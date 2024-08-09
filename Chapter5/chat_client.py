import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

client.connect(('127.0.0.1', port))
print("start client...")

while True:
    data = input("Please input msg:")
    if not data:
        break
    client.send(data.encode('utf-8'))
    client_data = client.recv(1024)
    if not client_data:
        break
    print("client receive: ", client_data.decode('utf-8'))

client.close()
