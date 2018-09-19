# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 协程.py 18-4-9 下午6:01
# SITE: https:www.jetbrains.com/pycharm/
from time import sleep

def testA():
    while True:
        print("-----A")
        yield
        sleep(0.5)

def testB(c):
    while True:
        print("----B")
        next(c)
        sleep(0.5)

if __name__ == "__main__":
    c = testA()
    testB(c)