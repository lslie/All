# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 线程同步.py 18-4-9 上午8:35
# SITE: https:www.jetbrains.com/pycharm/
from threading import Thread, Lock
from time import sleep

lock = Lock()
lock1 = Lock()
num = 10000


def text_one():
    lock.acquire()
    global num
    for i in range(1000000):
        num += i
        i += 1
    print("一", num)
    sleep(1)
    lock.release()


def test_two():
    lock.acquire()
    global num
    for i in range(1000000):
        num += i
        i += 1
    print("二", num)
    sleep(1)
    lock.release()


if __name__ == "__main__":
    t1 = Thread(target=text_one)
    t1.start()
    t2 = Thread(target=test_two)
    t2.start()
