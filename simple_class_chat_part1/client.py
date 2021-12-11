import socket
import sys

# create socket for communication
client_socket = socket.socket()

# get information to connect with the server
server_host = input("Enter server IP address you want to connect: ")
name = input("Enter your name: ")
port = 1234

print(f"Trying to connect to server: {server_host}, with {port}")
# connect with server through socket
client_socket.connect((server_host, port))
client_socket.send(name.encode())

# wait for acknowledgement from server
server_name = client_socket.recv(1024).decode()
print(f"'{server_name}' has joined.") 
print("Enter 'bye' to leave the chat room.")
print("------------------------------------")

# send and receive message from server
while True:
    message = client_socket.recv(1024).decode()
    print(f"{server_name}: {message}")
    message = input("Me: ")
    if message == 'bye':
        message = "Leaving the chat room."
        client_socket.send(message.encode())
        break
    client_socket.send(message.encode())