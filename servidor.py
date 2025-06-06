import socket
import threading
import os

def verificar_portas(ip):
    portas_a_testar = [22, 80, 443, 3389]
    abertas = []
    for porta in portas_a_testar:
        tomada = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tomada.settimeout(0.5)
        resultado = tomada.connect_ex((ip, porta))
        if resultado == 0:
            abertas.append(porta)
        tomada.close()
    return abertas

def ip_valido(endereco):
    try:
        socket.inet_aton(endereco)
        return True
    except socket.error:
        return False

def tratar_cliente(conexao, morada):
    try:
        nome_ficheiro = conexao.recv(1024).decode("utf-8").strip()

        if not os.path.exists(nome_ficheiro):
            conexao.send(f"Ficheiro '{nome_ficheiro}' não encontrado.".encode("utf-8"))
            conexao.close()
            return

        with open(nome_ficheiro, "r") as ficheiro:
            linhas = ficheiro.readlines()

        resposta_final = []
        for linha in linhas:
            linha = linha.partition("#")[0].strip()
            if not linha or not ip_valido(linha):
                continue
            ip = linha
            abertas = verificar_portas(ip)
            resposta_final.append(f"{ip} -> Portas abertas: {', '.join(map(str, abertas)) if abertas else 'nenhuma'}")

        resposta_texto = "\n".join(resposta_final)
        conexao.send(resposta_texto.encode("utf-8"))

    except Exception as erro:
        conexao.send(f"Ocorreu um erro: {str(erro)}".encode("utf-8"))
    finally:
        conexao.close()

def arrancar_servidor():
    anfitriao = "127.0.0.1"
    porta_escuta = 65432

    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.bind((anfitriao, porta_escuta))
    soquete.listen(5)

    print(f"[SERVIDOR] À escuta em {anfitriao}:{porta_escuta}...")

    while True:
        cliente, morada = soquete.accept()
        print(f"[SERVIDOR] Ligação estabelecida com {morada}")
        threading.Thread(target=tratar_cliente, args=(cliente, morada)).start()

if __name__ == "__main__":
    arrancar_servidor()
