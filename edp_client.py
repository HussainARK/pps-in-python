# Event-Driven Programming
# # Here we're creating the client Script that connects to the Server

import socket, threading

DISCONNECT_MESSAGE ="!DISCONNECT!"
HEADER = 2048

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)
print(f"[CLIENT] CONNECTED TO THE SERVER {SERVER_ADDR}")

def send(msg, sender_name):
    sender_name = str.encode(sender_name)
    client.send(sender_name)
    message = str.encode(msg)
    client.send(message)

def get_messages():
    messages = client.recv(HEADER).decode()
    print("\n" + messages)

sender = input('Enter your Name: ')

print(f'\n[CLIENT] to disconnect enter "{DISCONNECT_MESSAGE}" (without quotes)\n')

while True:
    threading.Thread(target=get_messages).start()
    message = input(f"{sender}> ")
    threading.Thread(target=get_messages).start()
    if message.strip() == "":
        threading.Thread(target=get_messages).start()
        pass
    else:
        threading.Thread(target=get_messages).start()
        if message == DISCONNECT_MESSAGE:
            threading.Thread(target=get_messages).start()
            send(message, sender)
            threading.Thread(target=get_messages).start()
            print(f"[CLIENT] DISCONNECTED to the SERVER {SERVER_ADDR}")
            threading.Thread(target=get_messages).start()
            exit()
        else:
            threading.Thread(target=get_messages).start()
            send(message, sender)
