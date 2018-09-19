# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# qq.py 18-4-9 下午8:25
# SITE: https:www.jetbrains.com/pycharm/
from threading import Thread
from socket import *

#shou
def recv_data():
    while True:
        recv_data,recv_aadress = udp.recvfrom(1024)
        print("%s>>:%s" % (recv_aadress,recv_data.decode("gb2312")),end="")
        print("<<:",end="")

#fa
def send_data():
    while True:
        send = input("<<:")
        udp.sendto(send.encode("gb2312"),("192.168.170.1",8080))
if __name__ == "__main__":
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(("",8888))

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)

    t1.start()
    t2.start()
    t1.join()
    t2.join()