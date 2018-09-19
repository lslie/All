# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# echo服务器.py 18-4-9 下午8:17
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from time import ctime

if __name__ == "__main__":
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(("",8888))
    num =1

    while True:
        recv_data,recv_adress = udp.recvfrom(1024)
        data = recv_data.decode("gb2312")
        udp.sendto(recv_data,recv_adress)
        print("已经吧%s条信息[%s]发送回去了" % (num,data))
        num+=1

    udp.close()