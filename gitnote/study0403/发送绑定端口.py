# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 发送绑定端口.py 18-4-2 下午9:37
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    cok = socket(AF_INET,SOCK_DGRAM)

    cok.bind(("192.168.110.1", 8888))
    send_msg = ("192.168.170.1",8080)

    senddate = "天王盖地虎".encode("gb2312")

    cok.sendto(senddate,send_msg)
    cok.close()