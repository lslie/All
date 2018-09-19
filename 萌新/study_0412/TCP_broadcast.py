# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# TCP_broadcast.py 18-4-11 下午7:21
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    udp = socket(AF_INET,SOCK_DGRAM)

    udp_address = "<broadcast>"

    udp.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

    while True:
        send_content = input("please cut you message:")

        if not send_content:
            print("your cut is not none!")
            continue

        send_content = "1:12312312312:meinv:mm-pc:32:%s" % send_content
        udp.sendto(send_content.encode("gb2312"),(udp_address,2425))

    udp.close()