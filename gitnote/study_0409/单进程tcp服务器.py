# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 单进程tcp服务器.py 18-4-9 上午8:59
# SITE: https:www.jetbrains.com/pycharm/
from socket import *

if __name__ == "__main__":
    # 创建serversocket
    sever_socket = socket(AF_INET, SOCK_STREAM)

    # 绑定端口号
    sever_socket.bind(("", 8899))
    # 设置端口服用
    sever_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 通过服务器监听客户端
    sever_socket.listen(5)
    # accept() 阻塞 socket.accept()----->new_socket,new_address
    sever_socket.setblocking(False) #设置false不阻塞当前accept()不会阻塞，没有客户端访问的情况下就会报错
    try:
        while True:
            try:
                new_socket, new_address = sever_socket.accept()
            except Exception as result:
                print("错误代码",result)
            else:
                print("有新客户链接",new_socket)
            new_socket.setblocking(False)#recv也不会阻塞
            # new_socket使用接收数据recv或者发送数据send,sendto
            while True:
                #recv是一个阻塞方法
                content = new_socket.recv(1024)
                content = content.decode("gb2312")
                print(content)

                if len(content) ==0:
                    print("客户端离开了")
                    new_socket.close()
                    break
    except Exception as result:
        print("错误代码",result)