#encoding=utf-8
from socket import *


def message(new_socket):
    #request 请求
    request = new_socket.recv(1024)
    print(request)
    new_socket.send(b'HTTP/1.1 200 OK\r\n\r\n')
    new_socket.send(b'i love you!\r\n')

def main():
    #创建套接字 AFipv4协议  S:流TCP
    sockets = socket(AF_INET,SOCK_STREAM)
    #绑定端口端口号65535个
    sockets.bind(("",8887))
    #设置监听数
    sockets.listen(5)

    while True:
        #接收到数据返回一个新socket 一个新地址
        new_socket,new_address = sockets.accept()
        #处理客户端数据
        message(new_socket)
        new_socket.close()



if __name__ == '__main__':
    main()