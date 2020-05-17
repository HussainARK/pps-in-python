# Event-Driven Programming
# # Here we're creating the client Script that connects to the Server

import socket, threading

DISCONNECT_MESSAGE ="DISCONNECTPLEASE!"
HEADER = 2048

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)
print(f"[CLIENT] CONNECTED TO THE SERVER {SERVER_ADDR}")

def send(msg):
    message = str.encode(msg)
    client.send(message)

print(f'\n[CLIENT] to disconnect enter "{DISCONNECT_MESSAGE}" (without quotes)\n')

while True:
    message = input("New Message> ")
    if message.strip() == "":
        pass
    else:
        if message == DISCONNECT_MESSAGE:
            send(message)
            print(f"[CLIENT] DISCONNECTED to the SERVER {SERVER_ADDR}")
            exit()
        else:
            send(message)
