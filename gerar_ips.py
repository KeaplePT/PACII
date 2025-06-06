import socket

PORTAS = [22, 80, 443, 3389]

def ip_valido(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def testar_portas(ip, portas):
    abertas = []
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        try:
            resultado = s.connect_ex((ip, porta))
            if resultado == 0:
                abertas.append(porta)
        except:
            pass
        finally:
            s.close()
    return abertas

def gerar_ips_rede(rede_base):
    ips_validos = []
    for i in range(1, 255):
        ip = f"{rede_base}.{i}"
        if not ip_valido(ip):
            continue
        portas_abertas = testar_portas(ip, PORTAS)
        if portas_abertas:
            print(f"[+] {ip} -> Portas abertas: {', '.join(map(str, portas_abertas))}")
            ips_validos.append(ip)
    return ips_validos

def guardar_ficheiro(ips, nome_ficheiro="ips.txt"):
    with open(nome_ficheiro, "w") as f:
        for ip in ips:
            f.write(ip + "\n")
    print(f"\n{len(ips)} IPs com portas abertas guardados em {nome_ficheiro}")

if __name__ == "__main__":
    base = "10.0.97"  # Sub-rede local
    print(f"📡 A verificar IPs na rede {base}.0/24...\n")
    lista = gerar_ips_rede(base)
    guardar_ficheiro(lista)
