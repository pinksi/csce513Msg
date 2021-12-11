import sys
import socket

print(f"Setting up the server.")

# get hostname, ip address from socket and set port
server = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the local port and connection address
server.bind((host_name, port))
print(f"Your IP address: {ip}; port: {port}")

name = input("Enter your name: ")
print("Waiting for incoming connections.")

# listen for client connection
server.listen(1)

# accept connection from client
connection, addr = server.accept()
print(f"Received connection from -> IP address: {addr[0]}, port: {addr[1]} | Connection Established.")

# get a connection from client side
client_name = connection.recv(1024).decode()

# send acknowledgement about connection
print(f"{client_name} has connected.")
print("Enter 'bye' to leave the chat room.")
print("------------------------------------")

# receive and send message to client
connection.send(name.encode())
while True:
    message = input("Me: ")
    if message == 'bye':
        message = "Connection End."
        connection.send(message.encode())
        break
    connection.send(message.encode())
    message = connection.recv(1024).decode()
    print(f"{client_name}: {message}")