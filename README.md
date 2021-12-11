# csce513Msg
### Design and develop an online chat system, named csce513Msg, for communications and discussions among students in a class.

#### 1. Client-Server Communication using TCP/IP 
Client-server that can communicate with each other through socket programming using TCP/IP. 
```
Usage: 

Run `server.py` [It shows the IP address of the server, and you can enter your name.] 

Run ‘client.py` [You need to enter the IP address of the server in the prompt and enter your name.] 
```

#### 2. Advanced Client 
Functionality to allow a client to send and receive messages at the same time.
```
Usage: 

Run `python server.py` 

Run `python client.py` 
```

#### 3. Multi-Thread Communication Server 
Allow multiple students to discuss class topics.
```
Usage: 

Run `python server.py` 

Run `python client.py` [You can run multiple client program in different terminal.] 
```

#### 4. Client-Client Communication 
Handles the cases in which if A wishes to chat with B, but B is not in system.
```
Usage: 

Run `python server.py` 

Run `python client.py` [You can run multiple client program in different terminal.] 
```

#### 5. Secure Communication 
Adding encryption to send messages securely.
```
Usage: 

Run `python server.py` 

Run `python clientA.py` to send the secret message. 

Run `python clientB.py` to receive the decrypted message.
```

#### 6. File Transfer
Transfer of files from client to server or vice versa.
```
Usage: 

Run `python server.py` 

Run `python client.py` 
```

#### 7. Group Chat
Each group members can send and recieve messages in the group chat window. The messages are visible to all group members.
```
Usage: 

Run the server: `python server.py` 

Run client: `python client.py`. You can run multiple clients in different terminals using the same command. 
```