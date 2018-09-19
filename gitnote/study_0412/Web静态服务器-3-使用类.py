# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# Web静态服务器-3-使用类.py 18-4-12 下午4:27
# SITE: https:www.jetbrains.com/pycharm
from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"
HTML_ROOT_JPG ="./img"


class HttpServer(object):
    def __init__(self):
        # 创建客户端
        self.tcp = socket(AF_INET, SOCK_STREAM)
        self.tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定端口
    def bind(self, port):
        self.tcp.bind(("", port))

    def start(self):
        # 设置监听
        self.tcp.listen(5)
        while True:
            new_socket, new_address = self.tcp.accept()
            print("客户已经链接")
            Process(target=self.handle_tcp, args=(new_socket,)).start()
            new_socket.close()

    # 客户
    def handle_tcp(self, new_socket):
        try:
            # 处理客户请求
            while True:
                recv_data = new_socket.recv(1024)
                response_line = recv_data.splitlines()
                for line in response_line:
                    print(line)

                response_start_line = response_line[0].decode("utf-8")
                # 获得html名字
                html_name = re.match("\w+ +(/[^ ]*)", response_start_line).group(1)
                # 判断html
                if html_name == '/':
                    html_name = "3.html"
                try:
                    f = open(HTML_ROOT_DIR+html_name, "r")
                except:
                    response_start_line = "HTTP/1.1 404 Found File\r\n"
                    response_heard = "Content-Type: " \
                                     "text/html;charset=utf-8\r\nMyServer: server\r\n"
                    response_body = "文件未找到"
                else:
                    html_read = f.read()
                    f.close()
                    response_start_line = "HTTP/1.1 200 OK\r\n"
                    response_heard = "Content-Type: " \
                                     "text/html;charset=utf-8\r\nMyServer: server\r\n"
                    response_body = html_read
                response_blank = "\r\n"
                response = response_start_line + response_heard + response_blank + response_body
                new_socket.send(response.encode("utf-8"))
                new_socket.close()
        except Exception as result:
            print("文件未找到",result)


def main():
    http = HttpServer()
    http.bind(9999)
    http.start()


if __name__ == "__main__":
    main()
