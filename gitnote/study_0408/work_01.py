# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# work_01.py 18-4-8 下午8:08
# SITE: https:www.jetbrains.com/pycharm/
#提示用户输入手机号码判断是否合法
import re
# tell = input("请输入您要查询的手机号码:")
# try:
#     tell_1 = re.match("([^0]\d{10})$",tell)
#     print(tell_1.group(),'输入正确')
# except Exception as result:
#     print("不合法，错误代码",result)

#邮箱等账号判断是否合法
if __name__ == "__main__":
    # email = "zhangxu@gmail.jpg"
    # try:
    #     email_ = re.match(r"(\w+)@(126|163|gmail).(com|cn)",email)
    #     print(email_.group())
    # except Exception as result:
    #     print("邮箱错误，错误代码：",result)

    # python_name = input ("请输入Python的变量名:")
    # try:
    #     python_names = re.match(r"([^A-Z|-])\w+",python_name)
    #     print(python_names.group())
    # except Exception as result:
    #     print("不是")
    # phone = input("请输入您的座机电话号码：")
    # phone_tell = re.match(r"(\d{3,4})(-?)(\d{8})",phone)
    # print(phone_tell.group())
    #str = "<html><h1>atguigu</h1></html>"
    # str1 = re.match(r"(<\w+><\w+>)(.+)(</\w+></\w+>)",str)
    # print(str1.group(2))

    #str1 = re.findall("\w+",str)
    #print(str1[2])

    # str = "python = 9999, c = 7890, c++ = 12345"
    # num = re.findall("\d+",str)
    # print(num)

    # str = "python = 997,java = 100"
    #
    # num = re.findall("\d+",str)
    # for i in num:
    #     i = int(i)
    #     i+=1
    #     print(i)

    html = '''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'''

    html_src = re.findall(r"https://.+?\.jpg",html)
    print(html_src)