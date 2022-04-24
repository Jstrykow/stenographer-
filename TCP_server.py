import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print(f'[*] nasłuchiwanie na {bind_ip}:{bind_port}')
    try: 
        while True:
            client, address = server.accept()
            print(f"[*] Przyjęto połączenie od {address[0]}:{address[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")


def handle_client(client_socket):
    with client_socket as sock:
        res = sock.recv(1024)
        # res = bytes(res, " utf-8")
        print(f"[*] Odebrano: {res}")
        sock.close()


if __name__ == "__main__":
    main()

"""
In the TCP header are flags, which can contain some bit of information,
for example, when we have two flags, we can send 2 bits
1 1, 0 0, 1 1, 1 0, etc for more info
"""
