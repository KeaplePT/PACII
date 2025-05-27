import dns.resolver
import socket

def is_dns_server(ip):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [ip]
        resolver.lifetime = 3
        resolver.resolve('google.com', 'A')
        return True
    except:
        return False

def main():
    ip = input("Enter the IP address to test: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    try:
        sock.sendto(b'', (ip, 53))
        print(f"Port 53 is open on {ip}.")
    except:
        print(f"Port 53 is not accessible on {ip}.")
        return
    finally:
        sock.close()

    if is_dns_server(ip):
        print(f"{ip} appears to be a valid DNS server.")
    else:
        print(f"{ip} does NOT appear to be a DNS server.")

if __name__ == "__main__":
    main()
