# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 简单的tcp服务器.py 18-4-10 上午12:22
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from threading import Thread

def recv_data(new_socket,new_adress):
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print(recv_data.decond("gb2312"))
        else:
            print("关闭客户端")
            break

def main():
    tcp_sever = socket(AF_INET, SOCK_STREAM)

    tcp_sever.bind(("", 9999))
    tcp_sever.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    tcp_sever.listen(5)
    try:
        while True:
            new_socket,new_adress = tcp_sever.accept()
            Thread(target=recv_data,args=(new_socket,new_adress)).start()
    finally:
        tcp_sever.close()

if __name__ == "__main__":
    main()
    # tcp_sever = socket(AF_INET,SOCK_STREAM)
    #
    # tcp_sever.bind(("",9999))
    # tcp_sever.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #
    # tcp_sever.listen(5)
    # while True:
    #
    #     #等待连接
    #     new_socket,new_adress = tcp_sever.accept()
    #     # 接收数据并且发送数据
    #     try:
    #         recv_data = new_socket.recv(1024)
    #         if len(recv_data) > 0:
    #             print(recv_data.decond("gb2312"))
    #
    #         else:
    #             print("客户端已经关闭")
    #             break
    #     finally:
    #         new_socket.close()
    #         print("关闭客户端",new_socket)
    # tcp_sever.close()