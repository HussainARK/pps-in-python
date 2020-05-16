# Event-Driven Programming
# # Example, Here we're creating a socket Server that clients can connect to and send messages to each other

import socket, threading, msvcrt

FORMAT = "utf-8"
DISCONNECT_MESSAGE ="!DISCONNECT!"

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def handle_client(connection, address):
    print(f"[SERVER] New Connection: {address}")
    with clients_lock:
        clients.add(connection)

    connected = True
    while connected:
        username = connection.recv(50).decode(FORMAT)
        msg = connection.recv(50).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            print(f"[{username}@{address[0]}] DISCONNECTED")
        else:
            listing = f"[{username}@{address[0]} NEW MSG] {msg}"
            with clients_lock:
                for client in clients:
                    client.send((listing + "\n").encode(FORMAT))
            print(listing)
    connection.close()

def start():
    server.listen()
    print(f"[SERVER] Listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
        print(f"[SERVER] Active Connections: {threading.activeCount() - 1}")


print('[SERVER] the Server is starting...')
start()
