# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 测试客户端.py 18-4-9 上午9:13
# SITE: https:www.jetbrains.com/pycharm/
import time
from socket import *

if __name__ == "__main__":
    #创建套接字
    client_socket = socket(AF_INET,SOCK_STREAM)
    #绑定端口
    client_socket.bind(("",9999))
    #设定要链接的网络服务器和端口号进行链接connect()
    ip_conent = ("192.168.170.128",8899)
    client_socket.connect(ip_conent)
    #反复发送十次信息
    for i in range(10):
        client_socket.send(("第"+str(i)+"次发送信息").encode("gb2312"))
        time.sleep(2)

    #关闭
    client_socket.close()