import socket

def DHCPScan(host: str) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(3)
    message = b'\x01\x01\x06\x00' + b'\x00' * 236
    try:
        s.sendto(message, (host, 67))
        s.recvfrom(1024)
        return True
    except:
        return False
    finally:
        s.close()
