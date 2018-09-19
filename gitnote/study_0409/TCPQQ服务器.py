# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# TCPQQ服务器.py 18-4-9 下午9:22
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from threading import Thread

def recv_data(new_socket,new_adress):
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print("来自%s:" % str(new_adress),end="")
            print(recv_data.decode("gb2312"))
        break

def send_data(new_socket):
    while True:
        sends = input("请输入您要发送的内容:")
        new_socket.send(sends.encode("gb2312"))
if __name__ == "__main__":
    tcp_lister = socket(AF_INET,SOCK_STREAM)
    tcp_lister.bind(("",8888))
    tcp_lister.listen(5)
    tcp_lister.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    while True:
        new_socket,new_adress = tcp_lister.accept()

        Thread(target=recv_data,args=(new_socket,new_adress)).start()

        Thread(target=send_data,args=(new_socket)).start()
    tcp_lister.close()


