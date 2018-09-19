# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 多线程聊天.py 18-4-2 下午8:44
# SITE: https:www.jetbrains.com/pycharm/
import socket
import threading
from threading import Thread


# 接受消息
def recv_message(udp_scoket):
    while True:
        recv_message = udp_scoket.recvfrom(1024)  # 设置缓存
        print(recv_message[1][0] + "发送过来的消息", recv_message[0].decode("utf-8"))


# 发送消息
def send_message(udp_socket):
    while True:
        message = input("请输入消息")
        send_message("192.168.21.32", 8082)
        udp_socket.sendto(message.encode("utf-8"), send_message)


if __name__ == "__main__":
    dup_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dup_soket.bind(("", 1128))
    Thread(target=recv_message, args=(dup_soket,)).start()
    Thread(target=send_message, args=(dup_soket,)).start()
