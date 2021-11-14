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
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        
        # request and store name
        client.send("NAME: ".encode('utf-8'))
        name = client.recv(1024)
        names.append(name)
        clients.append(client)

        # print and broadcast name
        print(f"Name of the client is {str(name)}")
        broadcast(f"{str(name)} joined! \n".encode('utf-8'))
        client.send("Connected to the server! \n".encode("utf-8"))

        # start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()    

if __name__ == '__main__':
    HOST = '127.0.0.1' 
    PORT = 9090

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))

    server.listen()

    # list of clients (students) and their names
    clients = []
    names = []

    print("Server running!!!!")
    receive()