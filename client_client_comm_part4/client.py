import threading 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(('127.0.0.1', 55451))

def client_receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        if "|" in message:
            val = message.split("|")
            for i in val:
                if i != "":
                    print(f"<{i}>")
        elif not message:
            break
        elif message == f'Left the room!':
            client.close()
            break
        else:
            print(message)
        
def client_send():
    name = input(str("Enter your name: "))
    client.send(name.encode())

    while True:
        message = input(str(""))
        if message == f'bye':
            message3 = "Leaving the chat room."
        else:
            message2 = input(str(f"<To: {message}>"))
            message3 = message + "|" + message2
        client.send(message3.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
client_send()
