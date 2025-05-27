import socket
import threading

def handle_connection(conn, addr, port_type):
    conn.recv(1024)
    if port_type == "open":
        conn.send(b"Fake service banner\r\n")
    conn.close()

def HoneyScan(host: str, openPort: int, closedPort: int):
    def start_listener(port, port_type):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, port))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                threading.Thread(target=handle_connection, args=(conn, addr, port_type)).start()
        except:
            pass
        finally:
            s.close()

    threading.Thread(target=start_listener, args=(openPort, "open"), daemon=True).start()
    threading.Thread(target=start_listener, args=(closedPort, "closed"), daemon=True).start()

    input("Honeypot running. Press Enter to stop...\n")
