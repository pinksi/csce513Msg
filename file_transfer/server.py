import os
import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 1234
SIZE = 1024

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_IP, TCP_PORT))
    server.listen()
    print("Server is listening...")

    # check if server_data directory exists
    if not os.path.isdir("server_data/"):
        os.makedirs("server_data/")

    while True:
        conn, addr = server.accept()
        print(f"New Client {addr} connected.")

        # receiving filename from client
        file_name = conn.recv(SIZE).decode('utf-8')
        print("Receiving filename.")
        file = open("server_data/"+file_name, "w")
        conn.send(f"The filename: {file_name} sent by client is well-received.".encode('utf-8'))

        # receiving file data from client
        print("Recieving file data.")
        data = conn.recv(SIZE).decode("utf-8")
        file.write(data)
        conn.send("The file data sent by client is well-received.".encode("utf-8"))

        # closing the file
        file.close()
        # closing connection from client
        conn.close()
        print(f"Client: {addr} disconnected.")
    server.close()

if __name__ == "__main__":
    main()
