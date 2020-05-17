# Event-Driven Programming
# # Example, Here we're creating a socket Server that clients can connect to and send messages to each other

import socket, threading

DISCONNECT_MESSAGE ="!DISCONNECT!"
HEADER = 2048

HOST = "127.0.0.1"
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
        username = connection.recv(HEADER).decode()
        msg = connection.recv(HEADER).decode()
        if msg == DISCONNECT_MESSAGE:
            connected = False
            with clients_lock:
                if clients != []:
                    for client in clients:
                        if client:
                            client.send(str.encode(f"[{username} DISCONNECTED]" + "\n"))
            print(f"[{username}@{address[0]}] DISCONNECTED")
        else:
            with clients_lock:
                for client in clients:
                    client.send(str.encode(f"[{username}] {msg}\n"))
            print(f"[{username}@{address[0]} NEW MSG] {msg}")
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
