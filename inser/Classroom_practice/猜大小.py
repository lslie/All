# -*- coding: UTF-8 -*-
def size_big():
    import random
    sum_l=int(random.randint(0,50))
    for i in range(1,4):
       num=int(input("请输入数字："))
       if num>sum_l:
           print("您输入的数字为%d,系统数字为%d"%(num,sum_l))
           print("猜错了")
           print("你还有%d"%(3-i))
       elif num<sum_l:
           print("您输入的数字为%d,系统数字为%d"%(num,sum_l))
           print("猜错了")
           print("你还有%d"%(3-i))
       elif num==sum_l:
           print("您输入的数字为%d,系统数字为%d"%(num,sum_l))
           print("猜对了")
           break
size_big()
