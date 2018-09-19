# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# TCPQQ.py 18-4-11 下午8:02
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from threading import Thread

def recv_data():
    while True:
        recv_message = tcp_client.recv(1024)
        if len(recv_message) > 0:
            print(recv_message.decode("gb2312"))

        else:
            break

def send_data():
    while True:

        send_message = input("请输入您要发送的内容:")

        tcp_client.send(send_message.encode("gb2312"))

if __name__ == "__main__":
    tcp_client = socket(AF_INET,SOCK_STREAM)

    tcp_client.connect(("192.168.170.130",8888))

    Thread(target=recv_data).start()
    Thread(target=send_data).start()

