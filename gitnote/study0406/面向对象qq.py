# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 模拟QQ.py 18-4-6 下午7:17
# SITE: https:www.jetbrains.com/pycharm/
from socket import AF_INET, socket, SOCK_DGRAM
import os, time
from threading import Thread


class RecvData(Thread):
    def __init__(self, udp):
        super().__init__()
        self.udp = udp

    def run(self):
        self.recv_data()  # 接收消息

    def recv_data(self):
        while True:
            recv = self.udp.recvfrom(1024)
            print(">>来自%s:%s" % (str(recv[1]), recv[0].decode("gb2312")))
            f = open("data.txt", "a+")
            f.write(recv[0].decode("gb2312"))
        f.close()


class SendData(Thread):
    def __init__(self, udp, targe_host, targe_port):
        super().__init__()
        self.udp = udp
        self.targe_host = targe_host
        self.targe_port = targe_port

    def run(self):
        self.send_data()

    # 发送数据
    def send_data(self):
        while True:
            send_conent = input("请输入发送:")
            self.udp.sendto(send_conent.encode("gb2312"), (self.targe_host, self.targe_port))
            writ = open("deta.txt", "a+")
            writ.write(send_conent)
        writ.open()


def main():
    # 套接字
    udp = socket(AF_INET, SOCK_DGRAM)
    udp.bind(("", 9991))
    targe_host = input("请输入你要链接的ip：")
    targe_port = input("请输入您要链接的端口号:")
    # 开启两个线程
    t1 = SendData(udp, targe_host, targe_port)
    t2 = RecvData(udp)
    t1.start()
    t2.start()
    t1.join()
    udp.close()


if __name__ == "__main__":
    main()
