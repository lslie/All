# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 实现收发.py 18-4-2 下午10:02
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    cok = socket(AF_INET,SOCK_DGRAM)

    cok.bind(("", 8888))

    send_ip = ("192.168.179.1",8088)

    send_mag = input("输入您要发送的内容：")
    cok.sendto(send_mag.encode("gb2312"),send_ip)

    recv_msg = cok.recvfrom(1024)
    print(recv_msg[0].decode("gb2312"))

    cok.close()