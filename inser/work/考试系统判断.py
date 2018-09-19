#从键盘获取用户名和密码。然后进行判断，如果正确就输出不正确就报错
name=input("请输入您的用户名：")
message=input("请输入您的密码：")
if(name!="张三" or message!="123456"):
    print("您输入的用户名或者密码有错。请重新输入")
else:
    print("亲爱的%s，欢迎登陆尚硅谷考试系统"%name)
