# Event-Driven Programming
# # Here we're creating the client Script that connects to the Server

import socket

FORMAT = "utf-8"
DISCONNECT_MESSAGE ="!DISCONNECT!"
HEADER = 2048

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)
print(f"[CLIENT] CONNECTED TO THE SERVER {SERVER_ADDR}")

def send(msg, sender_name):
    sender_name = sender_name.encode(FORMAT)
    client.send(sender_name)
    message = msg.encode(FORMAT)
    client.send(message)

sender = input('Enter your Name: ')

print('''\
[CLIENT] Enter "h" for help
''')

while True:
    user_input = input(f"{sender}> ")
    if user_input == "s":
        new_message = input('Message: ')
        send(new_message, sender)
        pass

    elif user_input == "h":
        print("""\
[CLIENT] Enter
    "s" to send a message,
    "d" to disconnect from the server,
    "l" to list live messages,
    "h" for displaying this message
""")

    elif user_input == "d":
        send(DISCONNECT_MESSAGE, sender)
        print(f"[CLIENT] DISCONNECTED to the SERVER {SERVER_ADDR}")
        exit()
    
    elif user_input == "l":
        print("[CLIENT] Getting recent messages...")
        listings = client.recv(HEADER).decode()
        print(listings)
    else:
        pass
