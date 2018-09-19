# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 显示html页面.py 18-4-12 下午3:06
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket, AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"
JPG_ROOT_DIR="./img"

def heard_clink(new_socket):
    try:
        while True:
            recv_data = new_socket.recv(1024)
            print(recv_data)
            response_line = recv_data.splitlines()
            for line in response_line:
                print(line)

            # 从b'GET /index.html HTTP/1.1'取html
            response_start = response_line[0].decode("utf-8")
            # 使用正则表达式寻找得到请求路径或者html
            file_name = re.match(r"\w+ +(/[^ ]*)", response_start).group(1)

            if file_name == '/':
                file_name = "3.html"

            file_path = HTML_ROOT_DIR + file_name
            print(file_path)
            # 解决文件不存在的问题
            try:
                f = open(file_path, "rb")
            except:
                response_start = "HTTP/1.1 404 Found File\r\n"
                response_heard = "Content-Type: " \
                                 "text/html;charset=utf-8\r\nMyServer: server\r\n"
                response_body = "文件未找到sorry"
            else:
                read_content = f.read()
                f.close()
                # 构造数据
                response_start = "HTTP/1.1 200 OK\r\n"
                response_heard = "Content-Type: " \
                                 "text/html;charset=utf-8\r\nMyServer: server\r\n"
                response_body = read_content
            response_blank = "\r\n"
            response_data = response_start + response_heard + response_blank + response_body
            new_socket.send(response_data.encode("utf-8"))
            new_socket.close()
    except Exception as result:
        print("文件未找到",result)

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind(("", 8887))
    tcp_socket.listen(5)
    try:
        while True:
            new_socket, new_address = tcp_socket.accept()
            Process(target=heard_clink, args=(new_socket,)).start()
            new_socket.close()
    finally:
        tcp_socket.close()


if __name__ == "__main__":
    main()
