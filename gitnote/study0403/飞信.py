# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 飞信.py 18-4-2 下午9:08
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    # 创建一个udp套接字，支持两台电脑间通讯
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定目标主机的端口
    send_address = ("192.168.21.26", 2425)
    # 发送内容
    address = input("请输入发送的消息").encode("gb2312")
    while True:
        udp_socket.sendto(address, send_address)
    # 关闭套接字
        udp_socket.close()
