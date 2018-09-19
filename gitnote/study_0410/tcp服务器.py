# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tcp服务器.py 18-4-10 上午8:37
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket,AF_INET,SOCK_STREAM,SOL_SOCKET,SO_REUSEADDR
from threading import Thread

def recv_data():
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print("来自%s:" % str(new_adress), end="")
            print(recv_data.decode("gb2312"))
        break

if __name__ == "__main__":
    tcp_socket = socket(AF_INET,SOCK_STREAM)

    tcp_socket.bind(("",8887))
    tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    tcp_socket.listen(5)
    while True:
        #设置等待接受消息
        new_socket,new_adress = tcp_socket.accept()


        Thread(target=recv_data,args=(new_socket,new_adress)).start()
    tcp_socket.close()