# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 广播.py 18-4-4 上午12:14
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

#创建一个udp的套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
#广播地址
#host = "<broadcast>"
host = "192.168.21.255"
send_address = (host,2425)
#设置成广播
udp_socket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    send_content = input("请输入您要发送的内容:")
    send_content = "1:12312312312:meinnv:mm-pc:32:"+send_content
#发送数据
    udp_socket.sendto(send_content.encode("gb2312"),send_address)
#关闭套接字
