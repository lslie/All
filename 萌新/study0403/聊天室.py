# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 聊天室.py 18-4-2 下午8:34
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from time import ctime
if __name__ == "__main__":
    eco = socket(AF_INET,SOCK_DGRAM)

    eco.bind(("", 8888))

    while True:
        reve_date = eco.recvfrom(1024)
        date = reve_date[0].decode("gb2312")
        print("来自%s：%s:%s")%((ctime(),str(reve_date[1]),date))
        eco.close()