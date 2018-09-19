# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# echo(回显)服务器代码和测试.py 18-4-9 下午3:07
# SITE: https:www.jetbrains.com/pycharm/
from socket import AF_INET,socket,SO_REUSEADDR,SOCK_STREAM,SOL_SOCKET
from select import select
def main():
   #创建tcp的socket套接字
   server_socket = socket(AF_INET,SOCK_STREAM)
   server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
   #绑定端口
   server_socket.bind(("",9999))
   #设置监听
   server_socket.listen(5)
   #客户端列表
   socket_lists = [server_socket]
   try:

      while True:
         #检测列表client_lists那些socket可以接收数据,
         #检测列表[]那些套接字(socket)可否发送数据
         #检测列表[]那些套接字(socket)是否产生了异常
         print("select--111")
         #这个select函数默认是堵塞,当有客户端链接的时候解除阻塞,
         # 当有数据可以接收的时候解除阻塞,当客户端断开的时候解除阻塞
         readable, wirteable,excep = select(socket_lists,[],[])
         # print("select--2222")
         # print(111)
         for sock in readable:
            #接收数据
            if sock == server_socket:
               print("sock == server_socket")
               #有新的客户端链接进来
               new_socket,new_address = sock.accept()
               #新的socket添加到列表中,便于下次socket的时候能检查到
               socket_lists.append(new_socket)
            else:
               # print("sock.recv(1024)....")
               #此时的套接字sock是直接可以取数据的
               recv_data = sock.recv(1024)
               if len(recv_data) > 0:
                  print("从[%s]:%s" % (str(new_address),recv_data))
                  sock.send(recv_data)
               else:
                  print("客户端已经断开")
                  #客户端已经断开,要移除
                  sock.close()
                  socket_lists.remove(sock)



   finally:
      #关闭套接字
      server_socket.close()

if __name__ == "__main__":
   main()
