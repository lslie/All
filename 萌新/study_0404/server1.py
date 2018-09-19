# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# server1.py.py 18-4-4 上午10:00
# SITE: https:www.jetbrains.com/pycharm/

'''
    1.准备服务端IP地址和端口号
    2.创建socket套接字
    3使用套接字与IP和端口号建立连接
    4.进行通讯
    5.关闭
'''
import socket
ip = '192.168.21.26'
hosts = 8899
send_address = (ip,hosts)
#创建套接字
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.bind(("", hosts))

#使用套接字与IP和端口号建立链接
test = client_socket.connect(send_address)
print("客户端",test)

client_socket.close()
