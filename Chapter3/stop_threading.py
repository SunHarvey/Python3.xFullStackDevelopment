import threading, time


class TeatThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        count = 1
        threadName = threading.current_thread().getName()
        while self._running:
            print("threadName= {0},count={1}".format(threadName, count))
            count += 1
            time.sleep(1)


if __name__ == '__main__':
    thr1 = TeatThread()
    thr1.start()
    time.sleep(3)

    thr1.terminate()
    print("主线程结束")
