import time, os

# print('fork1 pid={0}'.format(os.getpid()))
# time.sleep(60)
# print("OK")

pid = os.fork()
if pid == 0:
    print(pid)
    print("子进程(pid={0}),对应的父进程id={1}".format(os.getpid(), os.getppid()))
else:
    print(pid)
    print("父进程(pid={0}),生成了子进程(cpid={1})".format(os.getpid(), pid))

time.sleep(6)
print("OK")
