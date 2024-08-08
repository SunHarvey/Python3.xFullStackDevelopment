import multiprocessing
import time, os


class MultiProcessing(multiprocessing.Process):
    def __init__(self, name, num):
        multiprocessing.Process.__init__(self)
        self.name = name
        self.num = num

    def handle(self, name, num):
        for i in range(num):
            print("子进程运行中,name={0},i={1},pid={2},ppid={3}".format(name, i, os.getpid(), os.getppid()))

    def run(self):
        self.handle(self.name, self.num)


if __name__ == '__main__':
    print("父进程 %d" % os.getpid())
    p1 = MultiProcessing('python',2)
    p2 = MultiProcessing('java', 3)
    p1.start()
    p2.start()
    print("父进程将要执行")
    p1.join()
    p2.join()
    print("子进程已结束")
    time.sleep(10)
    print("父进程已结束")
