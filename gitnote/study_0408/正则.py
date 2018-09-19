# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 正则.py 18-4-8 上午9:45
# SITE: https:www.jetbrains.com/pycharm/
import re

if __name__ == "__main__":
    #0-100,不能出现以0开头
    #sun = re.match("[1-9]\d$|0$|100$",'0')
    #sun = re.match("[1-9]?\d?$|100$","101")
    #num = "<h1>你好世界</h1>"
    #sun = re.match("<h1>(.+)</h1>",num)
    #print(sun.group())
    #print(sun.group(1))
    #print(sun.groups()[0])根据下标获取元祖的值
    #校验邮箱
    #email = "hajh@qq.com"
    #sun = re.match("(\w+|\w{4,20})@(163|126|qq|gmail)\.(com|cn|net)$", email)
    #print(sun.groups()[1], end="")

    #pict = "gril.jpg"
    #sun = re.match("(.+)(jpg|png|gif|bmp)$",pict)
    #print(sun.groups(), end="")

    #电话号码
    # number = "010-12345678"
    # try:
    #     sun = re.match("([^-\D]*|(0\d{2,3}))-(\d{8})$",number)
    #     print(sun.groups())
    # except Exception as result:
    #     print("输入错误错误代码：",result)
    # ip = "192.168.21.26"
    #{3}引用前面3次
    # num = re.match(r"(\d{1,3})(.\1){3}$",ip)
    # print(num.group())
    # html = "<html><h1> 字符串</h1></html>"
    #
    # sun = re.match(r"<(.+)><(.+)>.*</\2></\1>",html)
    #
    # print(sun.groups())
    #<?P<别名>)---->(?P=别名)
    # concent = "<html><body>哈哈哈</body><html>"

    # sun = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",concent)

    # print(sun.groups())
    pass


