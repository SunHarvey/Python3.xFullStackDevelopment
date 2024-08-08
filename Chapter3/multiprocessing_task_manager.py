import random
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

task_queue = Queue()
result_queue = Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(1, 10000)
        print("PUt task %d" % n)
        task.put(n)
    print("Try get results.")
    for i in range(10):
        r = result.get(timeout=10)
        print("Result: %s" % r)

    manager.shutdown()
