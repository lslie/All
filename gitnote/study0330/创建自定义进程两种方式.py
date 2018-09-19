import os
import time
from multiprocessing import Process
#请用二种方式创建进程，并且说明和打印他们的进程id和父进程id。
#需要参考自定义进程类
#fork
# pid=os.fork()
# print('pid',pid)
# if pid==0:
#     print("子进程id=",os.getpid())
# elif pid>0:
#     print("父进程id=",os.getppid())
# else:
#     print("创建进程失败")
num = 10


def test():
    while True:
        time.sleep(1)


if __name__ == "__main__":
    # 使用process创建进程
    p = Process(target=test)
    # 开始执行进程
    p.start()
    while True:
        time.sleep(1)
        num += 1
        print("num=", num)
        print('num',os.getpid())
