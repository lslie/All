# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 单进程tcp客户端.py 18-4-9 上午10:21
# SITE: https:www.jetbrains.com/pycharm/
import time
from socket import *

# 创建客户端套接字
client_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
# client_socket.bind(("", 9999))  # 客户端自己的端口号
# 设定要连接的网络服务器和端口号进行连接connect()
send_address = ("192.168.170.128", 8899)
client_socket.connect(send_address)  # 进行三次握手
# 反复发送十次信息
for i in range(10):
    client_socket.send(("第"+str(i)+"次给服务器发送信息").encode("utf-8"))
    time.sleep(0.2)
# 关闭
client_socket.close()