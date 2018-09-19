# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# tftp协议下载文件.py 18-4-3 下午11:32
# SITE: https:www.jetbrains.com/pycharm/
from socket import socket, AF_INET, SOCK_DGRAM
from struct import pack, unpack

# 创建一个udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 发送的数据-》打包成网络的二进制
# !代表安装网络数据组织
# H把1替换成占有2个字节
# 8s,文件test.jpg的字符串的长度,7s
# 用b替换倒数第二个0,占1个字节
sendcontent = pack("!H8sb5sb", 1, "9178.jpg".encode("utf-8"), 0, b"octet", 0)
# 发送数据
send_address = ("192.168.21.27", 69)
# 发给tftp协议的服务器
udp_socket.sendto(sendcontent, send_address)


while True:
    # 接收来自服务器的数据最大为1024
    # recv_data数据---》（操作码+序列号）+“数据”
    recv_data, recv_address = udp_socket.recvfrom(1024)
    #print(recv_data, recv_address)
    recv_data_length = len(recv_data)

    # 把数据切片得到前---》（操作+数据块序列号）
    # 操作码：1上传2下载3正常数据4 响应吗5出错了
    code_packnum = recv_data[:4]

    #拆包--->code操作码和packnum数据块序列号
    code,packnum = unpack("!HH",code_packnum)
    #print(code,packnum)

    if code == 3:

        if packnum == 1:
            #创建新的空白文件
            recv_file = open("9178.jpg","wb")
        pack_data = recv_data[4:]
        pack_data_fmt = "!%ds" % len(pack_data)
        #解包后的数据
        data = unpack(pack_data_fmt,pack_data)
        recv_file.write(data[0])

        #向服务器发确认码ack
        send_ack = pack("!HH",4,packnum)
        #查看包的序号
        print("packnum==%s,reve_data_length==%s" % (packnum,recv_data_length))
        #开始发送
        udp_socket.sendto(send_ack,recv_address)

        if recv_data_length < 516:
            print("下载完成")
            recv_file.close()
            break
    elif code == 5:
        print("下载失败")
# 关闭套接字
udp_socket.close()
if __name__ == "__main__":
    pass
