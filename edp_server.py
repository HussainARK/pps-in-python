# Event-Driven Programming
# # Example, Here we're creating a socket Server that clients can connect to and send messages to each other

import socket, threading

HOST = "127.0.0.1"
PORT = 5050
ADDR = (HOST, PORT)

DISCONNECT_MESSAGE = "DISCONNECTPLEASE!"
HEADER = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(client_connection, client_address):
    print(f"[SERVER] New Connection: {client_address}")

    connected = True
    while connected:
        message = client_connection.recv(HEADER).decode()
        if message == DISCONNECT_MESSAGE:
            connected = False
            print(f"[{client_address}] DISCONNECTED")
        else:
            print(f"[{client_address} NEW MSG] {message}")
    client_connection.close()

print(f"[SERVER] Starting...")
server.listen()
print(f"[SERVER] Listening on {ADDR}")
while True:
    client_conn, client_addr = server.accept()
    threading.Thread(target=handle_client, args=(client_conn, client_addr)).start()
    print(f"[SERVER] Active Connections: {threading.activeCount() - 1}")
