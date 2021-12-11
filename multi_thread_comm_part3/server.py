import threading
import socket

TCP_host = '127.0.0.1'
TCP_port = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_host, TCP_port))
server.listen()

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

# handle the client connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f"{name} has left the chat room!".encode('utf-8'))
            names.remove(name)
            break

# receive the clients connection
def receive_msg():
    while True:
        print("Server is running and listening...")
        client, address = server.accept()
        print(f"Connection is established with {str(address)}")
        client.send('name:'.encode('utf-8'))
        name = client.recv(1024)
        names.append(name)
        clients.append(client)
        print(f"The name of this client is: {name}".encode('utf-8'))
        broadcast(f'{name} has connected to the chat room \n'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        print(f"List of connected clients: {names}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__=="__main__":
    receive_msg()