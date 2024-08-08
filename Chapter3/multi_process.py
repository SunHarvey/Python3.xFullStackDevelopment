from multiprocessing import Process
import time, os


def handle(name, num):
    for i in range(num):
        print("子进程中,name={0},i={1},pid={2},ppid={3}".format(name, i, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print("父进程 %d" % os.getpid())
    p1 = Process(target=handle, args=('python', 2))
    p2 = Process(target=handle, args=('java', 3))
    p1.start()
    p2.start()
    print("子进程将要执行")
    p1.join()
    p2.join()
    print("子进程已结束")
    time.sleep(5)
    print("父进程已结束")
