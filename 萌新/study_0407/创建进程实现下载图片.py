# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 创建进程实现下载图片.py 18-4-8 上午8:32
# SITE: https:www.jetbrains.com/pycharm/
# 创建进程实现下载图片
from threading import Thread
from multiprocessing import Pool
from time import sleep
from threading import Lock

# from socket import socket,AF_INET,SOCK_DGRAM

look = Lock()
look1 = Lock()


def text():
    look.acquire()
    for i in range(3):
        print("下载第%d张图片" % (i + 1))
    look1.release()


def pic():
    look1.acquire()
    for i in range(101):
        print("\r 下载%.2f%%" % i, end="\n")
        sleep(0.1)
    look.release()  # print("下载完成")


if __name__ == "__main__":
    pool = Pool(3)
    t1 = Thread(target=text)
    t1.start()
    try:
        for i in range(3):
            pool.apply(pic)
    except Exception as result:
        print("下载完成", result)
    # pool.join()

    pool.close()
    pool.join()
    print("下载完成")
