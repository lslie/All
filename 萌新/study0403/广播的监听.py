# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 广播的监听.py 18-4-4 上午12:28
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
# 代表电脑的任何一张网卡的ip地址
udp_socket.bind(("", 8888))
while True:
    recv_data, recv_address = udp_socket.recvfrom(1024)
    print("来自%s：%s" % (str(recv_address), recv_data.decode("gb2312")))

udp_socket.close()
