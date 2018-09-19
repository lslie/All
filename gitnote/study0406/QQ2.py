# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 模拟QQ.py 18-4-6 下午7:17
# SITE: https:www.jetbrains.com/pycharm/
from socket import AF_INET,socket,SOCK_DGRAM
import os,time
from threading import Thread
#目标主机
targe_host = None
#目标端口
targe_port = 0

udp = None
#接收消息
def recv_data():
    while True:
        recv = udp.recvfrom(1024)
        print(">>来自%s:%s" % (str(recv[1]),recv[0].decode("gb2312")))
        f = open("data.txt","a+")
        f.write(recv[0].decode("gb2312"))
    f.close()
#发送数据
def send_data():
    while True:
        send_conent = input("请输入发送:")
        udp.sendto(send_conent.encode("gb2312"),(targe_host,targe_port))
        writ = open("deta.txt","a+")
        writ.write(send_conent)
    writ.open()
def main():
    global targe_host
    global targe_port
    global udp

    #套接字
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(("", 9991))

    targe_host = input("请输入你要链接的ip：")

    targe_port = input ("请输入您要链接的端口号:")
    udp.close()
    #开启两个线程
    Thread(target=send_data).start()
    Thread(target=recv_data).start()

if __name__ == "__main__":
    main()