import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 1234
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_IP, TCP_PORT))
    
    # opening and reading the file data
    file = open("data/test.txt", "r")
    data = file.read()

    # sending filename to server
    client.send("test.txt".encode('utf-8'))
    msg = client.recv(SIZE).decode('utf-8')
    print(f"Message from Server: {msg}")

    # sending file data to server
    client.send(data.encode('utf-8'))
    msg = client.recv(SIZE).decode('utf-8')
    print(f"Message from Server: {msg}")

    # closing the file
    file.close()
    # closing connection from server
    client.close()


if __name__ == "__main__":
    main()