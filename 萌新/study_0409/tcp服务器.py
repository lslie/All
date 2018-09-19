# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tcp服务器.py 18-4-9 下午8:43
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket,AF_INET,SOCK_STREAM,SOL_SOCKET,SO_REUSEADDR

if __name__ == "__main__":
    udp = socket(AF_INET,SOCK_STREAM)

    udp.bind(("",8888))
    #socket.setsockopt(SOL_SOCKET, SO_REUSEADDR)
    #设置监听
    udp.listen(5)
    #等待连接

    new_socket,new_adress = udp.accept()
    while True:
        recv_data = new_socket.recv(1024)
        print(str(new_socket))
        print(recv_data.decode("gb2312"))
        new_socket.send("我来自tcp".encode("gb2312"))
    new_socket.close()
    udp.close()