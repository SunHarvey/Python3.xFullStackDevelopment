import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

server.bind(('127.0.0.1', port))
server.listen(10)
print("start socket server...")

while True:
    client, address = server.accept()
    print("new client connected!")
    msg = "connect to server successful"

    client.send(msg.encode("utf-8"))
    client.close()
# server.close()
