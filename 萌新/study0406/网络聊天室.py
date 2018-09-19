# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 网络聊天室.py 18-4-6 下午6:18
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from threading import Thread
from time import ctime
import os
#发消息
# def faxiaoxi():
#     udp = socket(AF_INET,SOCK_DGRAM)
#
#     udp.bind(("",8888))
#     udp_send = ("192.168.170.1",8080)
#
#     while True:
#         msg = input("发送消息：").encode("gb2312")
#         send_msg = (msg, udp_send)
#         re_cv = udp.recvfrom(1024)
#         print(re_cv[0].decond("gb2312"))
#     udp.close()
#收消息
def test():
    # 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 8887))
    # 发送位置
    # socket_ip = ("",1123)
    # 接收信息
    while True:
        socket_data = udp_socket.recvfrom(1024)
        #print("%s:%s:%s" % (ctime(), str(socket_data[1]), socket_data[0].decode("gb2312")))
        print(socket_data[0].decode("gb2312"))
        udp_socket.sendto(socket_data[0],socket_data[1])
        #使用encode服务器保存聊天记录
        f  = open("data.txt","a+")
        f.write(str(socket_data[0].decode("gb2312")))
        print("保存成功")
    f.close()
    udp_socket.close()
if __name__ == "__main__":
   # t2 = Thread(target=faxiaoxi)
    #t2.start()
    t1 = Thread(target=test)
    t1.start()