# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# encode服务器.py 18-4-6 下午6:46
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from time import ctime
def test():
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(("",8888))
    msg = input("请输入发送的消息：")
    send_ip = ("192.168.170.1",8080)
    send_msg = (msg,send_ip)
    #收消息
    while True:
        recv_msg = udp.recvfrom(1024)
        udp.sendto(recv_msg[0],recv_msg[1])
    print(send_msg[0],recv_msg[0])
    udp.clode()
if __name__ == "__main__":
    test()