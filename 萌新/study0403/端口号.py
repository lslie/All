# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 端口号.py 18-4-2 下午9:32
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    #创建借口
    cok = socket(AF_INET,SOCK_DGRAM)
    #设置发送的ip端口
    ads = ("192.168.21.23",2425)
    #发送人容
    senddate = "天王盖地虎".encode("gb2312")
    #
    cok.sendto(senddate,ads)
    cok.close()