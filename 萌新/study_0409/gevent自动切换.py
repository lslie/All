# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# gevent自动切换.py 18-4-9 下午6:54
# SITE: https:www.jetbrains.com/pycharm/
import gevent

def f(n):
    for i in range(n):
        print("%s:%s" % (gevent.getcurrent(),i))
        gevent.sleep(1)

if __name__ == "__main__":
    f1 = gevent.spawn(f,5)
    f2 = gevent.spawn(f,5)
    f3 = gevent.spawn(f,5)

    f1.join()
    f2.join()
    f3.join()