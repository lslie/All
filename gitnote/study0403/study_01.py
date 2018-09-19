# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# study_01.py 18-4-2 下午7:36
# SITE: https:www.jetbrains.com/pycharm/
import socket
if __name__ == "__main__":
    udp_socket = None
    try:

        udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #udp_socket.bind(("",8899))
        udp_socket.bind(("", 5215))
        rece_message = ("172.168.21.26",8899)
        sendadate = "小鸡炖蘑菇".encode("gb2312")
        udp_socket.sendto(sendadate,rece_message)
    except:
        print("发生错误")
    finally:
        #展示消息encode()编码decode()解码
        #print("--->",rece_message[0].decode('utf-8'))
        udp_socket.close()