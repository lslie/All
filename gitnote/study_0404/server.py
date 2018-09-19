# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# server.py 18-4-4 上午9:46
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    '''
    1.服务器端ip地址和端口号------>客户端
    2.服务器端也是一个套接字socket
            UDP  (socket (AF_INET,SOCK_DGRAM))
            tcp  socket(AF_INET,SOCK_STREAM)
    3.绑定IP和端口号
    4.设置socket监听listener
    5accpet()同意 ---->链接
    6.接收或者发送数据
    7.关闭
    '''
    #服务器端ip地址和端口号
    ip = '192.168.21.26'
    port = 8899

    #2.服务器也是一个套接字socket
    server_socket = socket(AF_INET,SOCK_STREAM)

    #绑定IP和端口号
    server_socket.bind(("", port))

    #设置socket监听listener
    server_socket.listen(3)

    #accpet()同意
    #阻塞式的方法有客户端调用的时候才不会阻塞
    new_socket,new_address = server_socket.accept()

    #关闭
    new_socket.close()
    server_socket.close()