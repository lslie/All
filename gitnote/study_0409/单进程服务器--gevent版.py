# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 单进程服务器--gevent版.py 18-4-9 下午7:05
# SITE: https:www.jetbrains.com/pycharm/
import sys
import time
import gevent
from gevent import socket,monkey
monkey.patch_all()

def hanadle_request(conn):
    while True:

        data = conn.recv(1024)
        print('11111')
        if not data:
            conn.close()
            break
        print("recv",data)
        conn.send(data)
def server(port):
    s = socket.socket()
    s.bind(("",port))
    s.listen(5)
    while True:

        new_Socket, addr = s.accept()
        print('222222')
        gevent.spawn(hanadle_request,new_Socket)

if __name__ == "__main__":
    server(7788)