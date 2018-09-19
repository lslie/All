# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 1.py 18-4-2 下午8:18
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
upd_socket = socket(AF_INET,SOCK_DGRAM)
#绑定
send_address = ("192.168.21.32",2425)
#发送
upd_socket.sendto("1:12312312312:mm:mm-pc:32:处处".encode("gb2312"),send_address)
#关闭
upd_socket.close()