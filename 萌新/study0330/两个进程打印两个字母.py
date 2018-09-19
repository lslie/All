import os
import time
from multiprocessing import Process


def test(name):
    for i in range(10):
        time.sleep(0.5)
        print('子进程运行中%s%d' % (name, i))


if __name__ == "__main__":
    # 创建进程
    p = Process(target=test, args=('te',))
    print("子进程马上开始")
    p.start()
    time.sleep(1)
    p.join()
    print("结束")
