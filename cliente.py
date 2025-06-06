import socket

def cliente_envia_ficheiro():
    anfitriao = "127.0.0.1"
    porta = 65432

    ficheiro = input("Nome do ficheiro com os IPs (ex: ips.txt): ").strip()

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((anfitriao, porta))

    cliente_socket.send(ficheiro.encode("utf-8"))

    resposta = cliente_socket.recv(8192).decode("utf-8")
    print("\n[RESULTADO DO SERVIDOR]:")
    print(resposta)

    cliente_socket.close()

if __name__ == "__main__":
    cliente_envia_ficheiro()
