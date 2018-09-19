# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# WAP服务器.py 18-4-10 上午8:57
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from multiprocessing import Process
def handle_client(new_socket):

    recv_data = new_socket.recv(1024)
        #回复信息
    response_line = "HTTP/1.1 200 OK\r\n"
    response_head = "server:MyGooGle\r\n"
    response_body = "<h1>welcome atguigu.com(whiteK)</h1>"
    response = response_line + "\r\n" + response_head + "\r\n" + response_body
    new_socket.send(response.encode("utf-8"))
        # if len(recv_data) > 0:
        #     print(recv_data.decode("gb2312"))
        # break
    new_socket.close()

def main():
    #创建套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # 设置端口复用
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #绑定端口
    tcp_socket.bind(("", 8889))

    #设置监听
    tcp_socket.listen(5)
    #等待客户连接
    new_socket,new_adress = tcp_socket.accept()
    print("新客户%s访问服务器" % str(new_adress))
    Process(target=handle_client,args=(new_socket,)).start()
    # new_socket.close()
    tcp_socket.close()
if __name__ == "__main__":
    main()