# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 服务器封装.py 18-4-10 下午4:13
# SITE: https:www.jetbrains.com/pycharm/
from socket import *
from multiprocessing import Process
# from study_0410 import ctime
import re
import sys

# 常量名大写重要
from typing import Any, Union
from wsgiref import headers

HTML_ROOT_DIR = "./html"


class Mains(object):
    response_hreader = ...  # type: Union[str, Any]

    def __init__(self):
        # 创建套接字
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        # 设置端口复用
        self.tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        # 绑定端口
        self.tcp_socket.bind(("", port))

    # 启动服务器
    def start(self):
        # 设置监听
        self.tcp_socket.listen(5)
        # 等待客户连接
        while True:
            new_socket, new_adress = self.tcp_socket.accept()
            print("新客户%s访问服务器" % str(new_adress))
            Process(target=self.handle_client, args=(new_socket,)).start()  # new_socket.close()  # tc
            new_socket.close()

    # 定义函数组织响应给浏览器的头信息 参数1:状态200, 400 302 500参数2：响应头
    def start_trsponse(self, status, header):
        response_hreaders = "HTTP/1.1 " + status + "\r\n"

        for header in headers:
            response_hreaders += "%s:%s" % header + "\r\n"
            # 赋值给实例对象的response_header,其他地方就能使用
            self.response_hreader = response_hreaders

    # 处理客户客户数据
    def handle_client(self, new_socket):
        recv_data = new_socket.recv(1024)
        # 回复信息
        s = recv_data.decode("gb2312")
        res_name = re.match(r"\w+ (/.*) ", s).group(1)
        file_name = res_name

        # 设置相应行响应头
        response_line = "HTTP/1.1 200 OK\r\n"
        response_head = "server:MyGooGle\r\n"

        # 添加动态判断判断是否.py结尾
        if file_name.endswith("py"):
            print("访问了一个py文件")
            model_name = file_name[1:-3]
            model = __import__(model_name)
            evn = {}
            response_body = model.applicatior(evn, self.start_trsponse)

        else:

            if res_name == "/" or res_name == "text.html":
                file_name = "text.html"

            f = None

            try:
                # 判断文件扩展名
                if file_name.endswith("html"):
                    f = open(HTML_ROOT_DIR + file_name, "rb")  # r--->str不用decode  rb-->使用decode解码成str
                elif file_name.endswith("jpg"):
                    f = open(HTML_ROOT_DIR + file_name, "rb")

                response_body = f.read()

            except:
                # 404
                response_line = "HTTP/1.1 404 Not Found\r\n"
                response_body = "文件找不到,sorry!"

            finally:
                if f != None:
                    f.close()
        # 200
        if isinstance(response_body, str):
            response = response_line + "\r\n" + response_head + "\r\n" + response_body
        elif isinstance(response_body, bytes):
            response = response_line + "\r\n" + response_head + "\r\n" + response_body.decode("gb2312")

        new_socket.send(response.encode("gb2312"))
        new_socket.close()




def main():
    http_server = Mains()
    http_server.bind(8888)
    http_server.start()


if __name__ == "__main__":
    main()
