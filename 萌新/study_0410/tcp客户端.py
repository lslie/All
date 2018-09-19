# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tcp客户端.py 18-4-10 上午8:33
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    tcp = socket(AF_INET,SOL_SOCKET)
    #发送地址
    tcp.connect(("192.168.170.129",8887))

    while True:
    #发送内容
        sends = input ("输入您要发送的内容:")
        tcp.send(sends.encode("gb2312"))

    tcp.close()
