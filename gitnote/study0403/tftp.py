# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tftp.py 18-4-3 上午1:34
# SITE: https:www.jetbrains.com/pycharm/
import  socket
from struct import pack,unpack

if __name__ == "__main__":
    udp_sockt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    send_content = pack("!H8sb5sb",1,"test.txt".encode("utf-8"),0,b"octet",0)
    send_msg = ("192.168.21.26",69)

    udp_sockt.sendto(send_content,send_msg)

    # content = udp_sockt.recvfrom(1024)
    # print(content)


    udp_sockt.close()
    #content = pack("!d",3.8)
    #print(content)