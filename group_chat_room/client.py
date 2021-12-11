import argparse

import socket
import threading
import tkinter # graphic interface library of python
import tkinter.scrolledtext
from tkinter import simpledialog

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()
        self.name = simpledialog.askstring("Username", "Please provide a name", parent=msg)
        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightblue")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightblue")
        self.chat_label.config(font=("Calibri", 12))
        self.chat_label.pack(padx=5, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win, width=50, height=10)
        self.text_area.pack(padx=5, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightblue")
        self.msg_label.config(font=("Calibri", 12))
        self.msg_label.pack(padx=5, pady=5)

        self.input_area = tkinter.Text(self.win, height=3, width=50)
        self.input_area.pack(padx=5, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Calibri", 12))
        self.send_button.pack(padx=5, pady=5)

        self.gui_done = True
        
        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    # send messages to server
    def write(self):
        message = f"{self.name}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)
    
    # listen to server and send name
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NAME: ':
                    self.sock.send(self.name.encode('utf-8'))
                if message == 'bye':
                    message = "Leaving the chat room."
                    self.sock.send(message.encode())
                    break
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')                        
                        self.text_area.config(state='disabled')

            except ConnectionAbortedError:
                break
            except:
                print("Error Occurred")
                self.sock.close()
                break    
        self.sock.close()

if __name__ == '__main__':
    TCP_IP = "127.0.0.1"
    TCP_PORT = 1234
    client = Client(TCP_IP, TCP_PORT)
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-ip", "--TCP_IP", help="Enter TCP IP address")
    # parser.add_argument("-p", "--TCP_PORT", type=int, help="Enter TCP port number")
    # args = parser.parse_args()
    # client = Client(args.TCP_IP, args.TCP_PORT)