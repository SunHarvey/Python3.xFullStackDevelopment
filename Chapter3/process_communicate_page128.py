from multiprocessing import Process, Queue
import time
import random


def write_queue(queue):
    print("start write queue")
    for i in range(5):
        print("write data = {0}".format(i))
        queue.put(str(i))
        time.sleep(random.random() * 5)
    print("write done")


def read_queue(queue):
    print("read queue")
    while True:
        data = queue.get()
        if data is None:  # 使用 None 作为终止信号
            break
        print("read data = {0}".format(data))
    print("read done")


if __name__ == '__main__':
    q = Queue()  # 实例化队列
    pw = Process(target=write_queue, args=(q,))
    pr = Process(target=read_queue, args=(q,))

    pw.start()
    pr.start()
    pw.join()

    q.put(None)  # 发送终止信号
    pr.join()  # 确保读取进程正常结束

    print("==== main process end ====")
