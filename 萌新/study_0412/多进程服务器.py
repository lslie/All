# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 多进程服务器.py 18-4-11 下午8:24
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from multiprocessing import Process



def  recv_data(new_socket,new_adress):

    while True:
        recv_message = new_socket.recv(1024)

        if len(recv_message) > 0:
            print("来自%s 的%s" % (str(new_adress),recv_message.decode("gb2312")))

        else:
            print("收到了信息")
            break



def send_data(new_socket):

    sen_message = input(":>>")
    new_socket.send(sen_message.encode("gb2312"))


def main():
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp_sock.bind(("",8888))
    tcp_sock.listen(3)
    try:
        while True:
            new_socket,new_adress = tcp_sock.accept()
            Process(target=recv_data,args=(new_socket,new_adress)).start()
            Process(target=send_data,args=(new_socket,))
            new_socket.close()
    finally:
        tcp_sock.close()
if __name__ == "__main__":
    main()