# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# epoll1.py 18-4-9 下午4:21
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
import select

def main():

   #创建tcp服务器套接字
   server_socket = socket(AF_INET,SOCK_STREAM)
   #设置端口可以重用
   server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
   #绑定端口
   server_socket.bind(("",9999))
   #设置监听
   server_socket.listen(5)

   #用epoll设置监听收数据
   epoll = select.epoll()
   #把server_socket注册到epoll的事件监听中,如果已经注册过会发生异常
   epoll.register(server_socket.fileno(),select.EPOLLIN|select.EPOLLET)
   #装socket列表
   socket_lists = {}
   #装socket对应的地址
   socket_address = {}
   while True:
      #返回套接字列表[(socket的文件描述符,select.EPOLLIN)],
      # 如果有新的链接,有数据发过来,断开链接等都会解除阻塞
      print("epoll.poll--111")
      epoll_list = epoll.poll()#[(文件描述符，注册的事件)]
      print("epoll.poll--222")
      print(epoll_list)
      for fd,event in epoll_list:
         #有新的链接
         if fd == server_socket.fileno():
            print("新的客户fd==%s" % fd)
            new_sokect,new_address = server_socket.accept()
            #往字典添加数据
            socket_lists[new_sokect.fileno()] = new_sokect
            socket_address[new_sokect.fileno()] = new_address
            #注册新的socket也注册到epoll的事件监听中
            epoll.register(new_sokect.fileno(), select.EPOLLIN | select.EPOLLET)
         elif event ==select.EPOLLIN:
            print("收到数据了")
            #根据文件操作符取出对应socket
            new_sokect = socket_lists[fd]
            address = socket_address[fd]
            recv_data = new_sokect.recv(1024)
            if len(recv_data) > 0:
               print("已经收到[%s]:%s" % (str(address),recv_data.decode("gb2312")))
            else:
               #客户端端口,取消监听
               epoll.unregister(fd)
               #关闭链接
               new_sokect.close()
               print("[%s]已经下线" % str(address))



   #关闭套接字链接
   server_socket.close()

if __name__ == "__main__":
   main()
