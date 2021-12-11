import threading
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 55451

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((TCP_IP, TCP_PORT))
print(f"Server bind to IP: {TCP_IP} Port: {TCP_PORT}")
server.listen()

clients = []
names = []
clients_lock  = threading.Lock()

# handle the client connections
def handle_client(client):
    with clients_lock:
        clients.append(client)

    name = client.recv(1024).decode()
    names.append(name)
    while True:
        string = ""
        if len(clients) == len(names):
            client.send("Enter any students from the list to connect with or type 'bye' to leave".encode())
            for i in range(len(clients)):
                if clients[i] == client:
                    continue
                string = string + "|" + names[i]
            client.send(string.encode())
            message = client.recv(1024).decode()
            if message == "bye":
                print(f"Client <{name}> is leaving the chat room...")
                clients.remove(client)
                names.remove(name)
                client.send("Left the room!".encode())
                break
            else:
                val = message.split("|")
                if not message:
                    break
                else:
                    flag = True
                    for i in range(len(clients)):
                        if val[0].lower() == names[i].lower():
                            target_client = i
                            flag = False
                            break
                    if flag == False:
                        with clients_lock:
                            if target_client <= len(clients):
                                for k in range(len(clients)):
                                    if clients[k] == client:
                                        print(f"Message from {names[k]} to {names[i]} >>> {val[1]}")
                                        clients[target_client].sendall(f"\n Message from {names[k]} >>> {val[1]}".encode())
                    else:
                        client.send(f"Requested user <<{val[0]}>> not found! Please choose another.".encode())
                        continue

# receive the clients connection
def receive_msg():
    while True:
        print("Server is running and listening...")
        client, address = server.accept()
        print(f"Connection is established with {str(address)}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__=="__main__":
    receive_msg()