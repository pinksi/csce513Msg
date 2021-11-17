import  socket
import threading

# sends messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# handle messages from clients 
def handle(client):
    while True:
        try:
            # broadcast message
            message = client.recv(1024)
            print(f"{names[clients.index(client)]}")
            broadcast(message)
        except:
            # removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'Client [{name}] left!'.encode('utf-8'))
            names.remove(name)
            break

# listen and accepts new connections/clients
def receive():
    while True:
        # accept connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {str(client_address)}!")
        
        # request and store name
        client_socket.send("NAME: ".encode('utf-8'))
        name = client_socket.recv(1024)
        names.append(name)
        clients.append(client_socket)

        # print and broadcast name
        print(f"Name of the client is {str(name)}")
        broadcast(f"{str(name)} joined! \n".encode('utf-8'))
        client_socket.send("Connected to the server! \n".encode("utf-8"))

        # start handling thread for client
        thread = threading.Thread(target=handle, args=(client_socket,))
        thread.start()    

if __name__ == '__main__':
    TCP_IP = '127.0.0.1'
    TCP_PORT = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((TCP_IP, TCP_PORT))

    server_socket.listen()

    # list of clients (students) and their names
    clients = []
    names = []

    print("Server running!!!!")
    receive()