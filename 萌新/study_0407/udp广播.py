# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# udp广播.py 18-4-7 下午1:49
# SITE: https:www.jetbrains.com/pycharm/
from socket import *


def main():
    udp = socket(AF_INET, SOCK_DGRAM)
    # 广播地址
    send_ip = "<broadcast>"

    udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    while True:
        send_input = input("请输入您要发送的内容:")

        send_input = "1:12312312312:meinv:mm-pc:32:%s" % send_input

        udp.sendto(send_input.encode("gb2312"), (send_ip, 2425))
    udp.close()


if __name__ == "__main__":
    main()
