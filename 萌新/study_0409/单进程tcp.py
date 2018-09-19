# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 单进程tcp.py 18-4-9 上午10:20
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
import time

# 创建serversocket
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口号
server_socket.bind(("", 8899))
# 设置端口复用
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# accept() 阻塞   socket.accept()  --->new_socket,new_address
server_socket.setblocking(False)  # 有客户端访问，当前的accept()不会阻塞 ，没有客户端访问的情况下就会报错

# 通过服务器监听客户端
server_socket.listen(5)

# 客户端列表
client_lists = []

try:
    while True:
        try:
            new_socket, new_address = server_socket.accept()
            print("1111---->socket")
        except Exception as result:
            # print("====>",result)
            pass
        else:
            print("有新客户连接上服务器了,新地址是:", new_address)

            client_lists.append((new_socket, new_address))

            new_socket.setblocking(False)  # recv也不会阻塞了
            # new_socket 使用接收数据recv或者发送数据send | sendto
            while True:
                try:
                    # time.sleep(1)
                    content = new_socket.recv(1024)  # --->阻塞方法  轮询
                    print("1111---->recv")
                except:
                    #print("*******")
                    pass
                else:
                    content = content.decode("utf-8")
                    print(content)
                    if len(content) > 0:
                        print("收到客户端信息:", content)

                    elif len(content) == 0:
                        print("客户端离开了")

                        new_socket.close()
                        break
finally:
    server_socket.close()
