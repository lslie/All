# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 服务器gevent协成版.py 18-4-11 下午11:42
from gevent import monkey,socket
import gevent
monkey.patch_all()


#相应数据函数
def handle_client(new_sock,new_address):
    try:
        while True:
            data = new_sock.recv(1024)
            print(data.decode("gb2312"))
            #构造相应数据响应行
            response_start_line = "HTTP/1.1 200 OK\r\n"
            #头
            response_headers = "Content-Type:text/html;charset=utf-8\r\n"
            #体
            response_body = "你好世界"
            # 拼接数据，注意响应头和响应体家\r\n
            response = response_start_line + "\r\n" + response_headers + "\r\n" + response_body
            print(response)
            new_sock.send(response.encode("gb2312"))
            new_sock.close()
    except Exception as result:
        pass

def main():
    tcp_socket = socket.socket()
    #tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_socket.bind(("",8887))
    tcp_socket.listen(128)
    try:
        while True:
            new_sock,new_address = tcp_socket.accept()
            print("已经链接")
        gevent(handle_client,new_sock,new_address)

    finally:
        tcp_socket.close()
if __name__ == "__main__":
    main()