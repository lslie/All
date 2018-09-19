# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# structunpack和写完接收数据.py 18-4-3 下午11:21
# SITE: https:www.jetbrains.com/pycharm/
from socket import AF_INET,socket,SOCK_DGRAM
from struct import pack,unpack

#创建udp套接字
udp_sokect = socket(AF_INET,SOCK_DGRAM)
#打包数据
#!这个数据是要在网络中传输的,按照网络方式封装包
#H,替换第一个1,并且占2个字节
#8s,占8个字节,代表test.jpg的长度,如果是afu.text那么就是7s,设置编码
#b占1个字节,替换0
#5s,占5个字节,替换octet,并且前面加上b,二进制
#s,占1个字节,替换最后一个0
send_content = pack("!H8sb5sb",1,"9718.jpg".encode("utf-8"),0,b"octet",0)
#发送请求的地址
send_address = ("192.168.1.18",69)
#发送请求
udp_sokect.sendto(send_content,send_address)


while True:

   recv_data,recv_address = udp_sokect.recvfrom(1024)
   data_length = len(recv_data)

   #得到操作码(4个字节)--包含操作码和编号
   code_num = recv_data[:4]
   #code操作码:1下载,2上传,3请求成功,4确认码,5错误码
   #num数据编号,从1开始
   code,num = unpack("!HH",code_num)
   if code == 3 :

      if num== 1:#第一次传递过来
         #创建文件
         f = open("test.jpg","wb")

      pack_data = recv_data[4:]
      # !网络数据方式解包数据,最终得到!512s
      format_data = "!%ds" % len(pack_data)
      #这才是解包好的数据,才可以写入
      data = unpack(format_data, pack_data)
      # if g_num+1 ==  num:

      f.write(data[0])

      #发确认包ack 4,发的时候也要装包
      send_ack = pack("!HH",4,num)
      #发送送数据
      udp_sokect.sendto(send_ack,recv_address)

      if data_length < 516:
         f.close()
         print("拷贝完成")
         break

   elif code ==5 :#出错了
      print("出错了")
      break

#关闭套接字
udp_sokect.close()
