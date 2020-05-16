# Event-Driven Programming
# # Here we're creating the client Script that connects to the Server

import socket

FORMAT = "utf-8"
DISCONNECT_MESSAGE ="!DISCONNECT!"
HEADER = 2048

SERVER_HOST = "192.168.0.102"
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

while True:
    print('''\
Enter "s" to send a message,
"d" to disconnect from the server,
"l" to list live messages
''')

    user_input = input()
    if user_input == "s":
        new_message = input('Message: ')
        send(new_message, sender)
        pass
    
    elif user_input == "d":
        send(DISCONNECT_MESSAGE, sender)
        print(f"[CLIENT] DISCONNECTED to the SERVER {SERVER_ADDR}")
        exit()
    
    elif user_input == "l":
        continue_listing = True
        while continue_listing:
            a_listing = client.recv(HEADER).decode()
            print(a_listing)
            input('Press "ENTER" to exit from listing\n')
            continue_listing = False
    else:
        pass
