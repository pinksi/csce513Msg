import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 9000

print(f"Waiting for secret message.")
clientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientB.connect((TCP_IP, TCP_PORT))
data = clientB.recv(1024)
secret_msg = data.decode()
clientB.close()
print(f"Secret message received: {secret_msg}")
print("Success.")