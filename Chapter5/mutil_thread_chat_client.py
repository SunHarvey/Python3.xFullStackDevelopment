import socket
import time
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))
msg = ''
running = True


def client_recv_msg():
    while running:
        msg = client.recv(1024).decode('utf-8')
        print("\nfrom sever receive: ", msg)
        time.sleep(1)


def send_msg():
    global running
    while running:
        msg = input("\nPlease enter your message: ")
        client.send(msg.encode('utf-8'))

        if msg == "quit":
            running = False
            break


if __name__ == '__main__':
    thr1 = threading.Thread(target=client_recv_msg, args=(), name="recv_thread")
    thr2 = threading.Thread(target=send_msg(), args=(), name="send_thread")
    thr1.start()
    thr2.start()
