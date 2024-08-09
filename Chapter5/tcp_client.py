import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
client.connect(('127.0.0.1', port))
print("start socket client...")

msg = client.recv(1024).decode('utf-8')
print("client received:", msg)
