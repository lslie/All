# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# ctime.py 18-4-10 下午4:33
# SITE: https:www.jetbrains.com/pycharm/
import time


def get_time():
    return time.ctime()


def application(evn,start_response):

    #调用传入进来的start_response函数
    #并且调用的时候吧当运行状态的相关状态给服务器
    status = "200 OK"
    headers = [
        ("Content-Type","Text/plain")
    ]
    start_response(status,headers)
    return get_time()
if __name__ == "__main__":
    print(get_time())