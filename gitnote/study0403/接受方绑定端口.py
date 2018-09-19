# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 接受方绑定端口.py 18-4-2 下午9:45
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    cok = socket(AF_INET,SOCK_DGRAM)

    cok.bind(("", 8888))
    #接受数据
    recv_message = cok.recvfrom(1024)
    print(recv_message)
    print(recv_message[0].decode("gb2312"))
    cok.close()