import socket
import threading
import sys

TCP_IP = "127.0.0.1"
TCP_PORT = 9000

name = input("Choose a name :: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

def recieve_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "name:":
                client_socket.send(name.encode('utf-8'))
            if not message:
                break
            print(message)
        except Exception as e:
            print(f'Error >> {e} >> occurred!')
            client_socket.close()
            break

def send_message():
    while True:
        message = f"{name}: {input()}"
        client_socket.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=recieve_message)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()