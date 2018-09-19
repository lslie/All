# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# epoll.py 18-4-9 下午3:51
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
import select

def main():

    #创建tcp服务器套接字
    sever_socket = socket(AF_INET,SOCK_STREAM)
    #设置端口可以重用
    sever_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #绑定端口
    sever_socket.bind(("", 9999))
    #设置监听
    sever_socket.listen(5)
    #用empoll设置监听收数据
    epoll = select.epoll()
    #把sever_socket注册到empoll的时间监听中，如果已经注册过会发生异常
    #监听的事件select.EPOLLIN | select.EPOLLET
    epoll.register(sever_socket.fileno(),select.EPOLLIN | select.EPOLLET)

    #装socket列表
    socket_lists = {}
    #床sockcet 对用的地址
    socket_address = {}
    while True:
        #返回套接字列表[（socket的文件描述符，select.EPOLLIN）],
        #如果有新的链接，有数据发过来，断开链接等都会接触阻塞
        print("empoll.poll---111")
        #文件描述符，注册的事件
        epoll_list = epoll.poll()

        print("empoll.poll----22")

        print(epoll_list)

        for fd,event in epoll_list:
            #有新的链接
            if fd == sever_socket.fileno():
                print("新用户fd == %s" % fd)
                new_socket,new_address = sever_socket.accept()
                #往字典加数据
                socket_lists[new_socket.fileno()] = new_socket
                socket_address[new_socket.fileno()] = new_address
                #注册新的socket也注册到epoll的事件监听中
                epoll.register(new_socket.fileno(),select.EPOLLIN | select.EPOLLET)

            elif event == select.EPOLLIN:
                print("收到数据了")
                #根据文件操作符取出对应的socket
                new_socket = socket_lists[fd]
                address = socket_address[fd]
                recv_data = new_socket.recv(1024)
                if len(recv_data) > 0:
                    print("已经收到[%s]:%s" %(str(address),recv_data.decode("gb2312")))

                else:
                    #客户端端口，取消监听
                    epoll.unregister(fd)
                    #关闭连接
                    new_socket.close()
                    print("[%s]已经下线" % str(address))

    sever_socket.close()
if __name__ == "__main__":
    main()