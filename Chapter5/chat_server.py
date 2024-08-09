import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

server.bind(('127.0.0.1', port))
server.listen(10)
print("start socket server...")
while True:
    client, address = server.accept()
    print("client connected:", address)
    while True:
        client_data = client.recv(1024).decode('utf-8')
        print("server receive msg:", client_data)

        if not client_data or client_data == 'quit':
            break
        msg = "server time is ={0}".format(time.ctime())
        client.send(msg.encode('utf-8'))
    client.close()
# server.close()
