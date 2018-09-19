#-*-coding:utf-8-*-
try:
    name=int(raw_input("请输入您的年龄："))
except ImportError:
    name=int(input("请输入您的年龄："))
print("=======if判断开始------")
if name>=18:
    print("我已经成年了，可以做成年人做的事情了")
print("----if判断语句结束------")
