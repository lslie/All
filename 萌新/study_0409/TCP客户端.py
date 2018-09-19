# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# TCP客户端.py 18-4-9 下午8:54
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    tcp = socket(AF_INET,SOCK_STREAM)

    tcp.connect(("192.168.170.129",8888))
    send_message = input(">>:")
    tcp.send(send_message.encode("gb2312"))
    while True:
        recv_data = tcp.recv(1024)

        print(recv_data.decode("gb2312"))

    tcp.close()