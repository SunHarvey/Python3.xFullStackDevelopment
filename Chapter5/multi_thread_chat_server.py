import threading
import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(5)
    print("server start...")

    while True:
        client, address = server.accept()
        print("client {0} connected".format(address))
        th1 = threading.Thread(target=recv_msg, args=(client, address))
        th1.start()


def recv_msg(client, address):
    while True:
        msg_bytes = client.recv(1024)
        msg = msg_bytes.decode("utf-8")
        print("from client {0} received: {1}".format(address, msg))

        if not msg or msg == "quit":
            print("close client {0}".format(address))
            client.close()
            break
        client.send(msg_bytes)


if __name__ == '__main__':
    main()
