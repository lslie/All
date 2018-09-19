import time
from multiprocessing import Process
import os

#小明  刷锅
def shua_guo(num,name):
    print("shuaguo------->",num)
    for i in range(num):
        print("%s很高兴的刷第%d遍锅" % (name,i))
        time.sleep(0.5)

#小花 扫地
def sao_di(num,name):
    print("saodi------->",num)
    for i in range(num):
        if i == 0:
            print("%s很高兴的扫地"%name)
        elif i >= 1:
            print("%s在拖地"%name)
        time.sleep(0.5)

if __name__ == "__main__":
    #创建进程
    p1=Process(target=shua_guo,args=(2,'小明'))
    p1.start()


    p2=Process(target=sao_di,args=(3,'小花'))
    p2.start()

    p1.join()
    p2.join()
for i in range(5):
    print("爸爸在高兴的看电视",i)