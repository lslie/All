# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# TC_qq客户端.py 18-4-11 下午8:09
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from threading import Thread


def recv_data(new_address,new_socket):
    while True:
        recv_message = new_socket.recv(1024)

        if len(recv_message) > 0:
            print("来自%s的消息%s" % (str(new_address),recv_message.decode("gb2312")))
        break


def send_data(new_socket):
    while True:

        send_message = input ("：>>")
        new_socket.send(send_message.encode("gb2312"))


if __name__ == "__main__":
    tcp_socket = socket(AF_INET,SOCK_STREAM)

    tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp_socket.bind(("",8888))

    tcp_socket.listen(3)
    while True:
        new_socket,new_address = tcp_socket.accept()

        Thread(target=recv_data,args=(new_address,new_socket)).start()
        Thread(target=send_data,args=(new_socket,)).start()

    tcp_socket.close()