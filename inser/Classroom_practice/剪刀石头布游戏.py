import random
player=int(input("请输入：剪刀（0）石头（1）布（2）:"))
computer=random.randint(0,2)
#用来进行测试
if((player==0)and(computer==2)or(player==1)and(computer==0)or(player==2)and(conputer==1)):
    print("获胜")
elif player==computer:
    print("平手")
else:
    print("输了")

