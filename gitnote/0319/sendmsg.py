#写一个自定义模块sendmsg.py，模块中有全局变量，函数，有类；
# 在另外一个模块main.py调用sendmsg.py模块中的变量和函数和类




num="这是全局变量"




class Text(object):
    def abc(self):
        print ("这是调用的类")




def hanshu(a,b):
    print("这是函数")
    return a+b
