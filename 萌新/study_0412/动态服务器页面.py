# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 动态服务器页面.py 18-4-11 下午11:25
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket,AF_INET,SO_REUSEADDR,SOCK_STREAM,SOL_SOCKET
from multiprocessing import Process


def handle_client(new_socket,new_address):
   recv_data = new_socket.recv(1024)
   print(recv_data)
   #响应行
   response_start = "HTTP/1.1 200 OK\r\n"
   #响应头
   response_headers = "Content-Type: text/html;charset=utf-8\r\nMyServer: server\r\n"
   #空行(\r\n)
   response_blank = "\r\n"
   #响应体(在浏览器展示的内容)
   response_body = "我来自web服务器,我要在浏览器显示了哦"
   #组装要返回的数据
   response_data = response_start+response_headers+response_blank+response_body
   print("response_data==", response_data)
   new_socket.send(response_data.encode("utf-8"))
   new_socket.close()


def main():
   #创建tcp服务器
   server = socket(AF_INET,SOCK_STREAM)
   #绑定端口
   server.bind(("",8888))
   #设置端口可以重复利用
   server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
   #设置监听
   server.listen(128)
   try:

      while True:
         new_socket,new_address = server.accept()
         print("[%s:%s]连接上" % new_address)
         p = Process(target=handle_client,args=(new_socket,new_address))
         p.start()
         #在主进程关闭new_socket
         new_socket.close()

   finally:
      server.close()


if __name__ == "__main__":
   main()
