import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 9000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((TCP_IP, TCP_PORT))
print(f"Server bind to IP: {TCP_IP} Port: {TCP_PORT}")

print("Waiting for incoming connections.")
server_socket.listen(1)

def send_message(conn):
    conn.send('name:'.encode('utf-8'))
    name = conn.recv(1024)
    print(f"The name of this client is: {name}".encode('utf-8'))
    while True:
        message = conn.recv(1024).decode()
        resend_msg = f"You [{name}] send this message: {message}"
        if not message:
            break
        conn.sendall(str.encode(resend_msg))
    conn.close()

while True:
    # accept connection from client
    client_connection, addr = server_socket.accept()
    print(f"Connection is established with {str(addr)}")
    send_message(client_connection)