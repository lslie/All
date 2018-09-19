# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tcpQQ.py 18-4-9 下午9:14
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread

def recv_data():
    while True:
        recv_data = tcp_socket.recv(1024)
        if len(recv_data) > 0:
            print(recv_data.decode("gb2312"))
        break

def send_data():
    while True:
        send_message = input("输入要发送的内容:")
        tcp_socket.send(send_message.encode("gb2312"))

if __name__ == "__main__":
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    tcp_socket.connect(("192.168.170.129",8888))
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    tcp_socket.close()