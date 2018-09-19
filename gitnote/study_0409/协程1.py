# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 协程1.py 18-4-9 下午6:17
# SITE: https:www.jetbrains.com/pycharm/
from greenlet import greenlet
from time import sleep

#from UnityTweakTool.elements import switch


def testA():
    while True:
        print("--------1111")
        sleep(0.5)
        g2.switch()
        print("----------22222")
        sleep(0.5)

def testB():
    while True:
        print("--------3333")
        sleep(0.5)
        g1.switch()
        print("---------44444")
        sleep(0.5)
if __name__ == "__main__":
    g1 = greenlet(testA)
    g2 = greenlet(testB)
    g1.switch()