from multiprocessing import Pool
import time, os, random


def worker(msg):
    t_start = time.time()
    print("任务%s开始执行,进程号为 %d" % (msg, os.getpid()))

    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("任务 %s, 执行完毕,耗时 %0.2f 秒" % (msg, (t_stop - t_start)))


if __name__ == '__main__':
    print("夫进程 %d." % os.getpid())
    pool = Pool(3)
    for i in range(0, 5):
        pool.apply_async(worker, (i,))
        # pool.apply(worker, (i,))
    pool.close()
    pool.join()
