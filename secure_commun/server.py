# sending encrypted message from client to server
import socket
import sys
from Cryptodome.Cipher import AES

TCP_IP = "127.0.0.1"
TCP_PORT = 9000
CIPHER_KEY = b"12345678sixteen!"
NONCE = b"12345678sixtee!!"

TCP_BUFFER = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(2)

connection1, address1 = server.accept()
print(f"Client A is connected from: {address1}")

connection2, address2 = server.accept()
print(f"Client B is connected from: {address1}")

while True:
    print(f"Receiving Secret Encrypted Message.")
    ciphertext = connection1.recv(TCP_BUFFER) #clientA sending cipher message
    print(f"Received Encrypted message: {ciphertext}")
    cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)
    plaintext = cipher.decrypt(ciphertext)
    connection2.sendall(plaintext)
    print(f"Decrypted message sent to Client B!")
    break

print("Success.")
server.close()