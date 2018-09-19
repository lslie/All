# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 飞信2.py 18-4-2 下午9:27
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    #创建接口
    udp_scoket = socket(AF_INET,SOCK_DGRAM)
    #目标主机
    send_add = ("192.168.21.26", 2425)
    #发送信息
    udp_scoket.sendto("1:12312312312:mm:mm-pc:32:你好".encode("gb2312"),send_add)

    udp_scoket.close()