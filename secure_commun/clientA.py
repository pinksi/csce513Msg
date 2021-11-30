# client to send encrypted data to another client
import socket
import sys
import re
import getpass
from Cryptodome.Cipher import AES

TCP_IP = "127.0.0.1"
TCP_PORT = 9000
CIPHER_KEY = b"12345678sixteen!"
NONCE = b"12345678sixtee!!"

clientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientA.connect((TCP_IP, TCP_PORT))

while True:
    secret_msg_input = getpass.getpass(prompt="Enter Secret Message here: ")
    print(f"Message will get Encrypted with AES.")
    raw_msg = secret_msg_input.encode()
    cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)
    ciphertext, tag = cipher.encrypt_and_digest(raw_msg)
    print(f"Sending encrypted message: {ciphertext}")
    clientA.send(ciphertext) # send ciphertext of raw message
    clientA.close()
    break

clientA.close()
print(f"Message sent. Success.")

