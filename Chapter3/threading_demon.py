import threading, time


def run(taskName):
    print("task:", taskName)
    time.sleep(2)
    print("task finished".format(taskName))


if __name__ == '__main__':
    start_time = time.time()
    for i in range(3):
        thr = threading.Thread(target=run, args=("task-{0}".format(i),))
        thr.setDaemon(True)
        thr.start()

    print("{0}线程结束，当前线程数量={1}".format(threading.current_thread().getName(), threading.active_count()))
    print("消耗时间:", time.time() - start_time)
