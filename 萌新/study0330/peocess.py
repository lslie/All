import time
from multiprocessing import Process

# 全局变量
num = 100
list=[0,2]


def test():
    print("我是test方法")
    for i in range(3):

        print("子进程------>i:%d,num:%d" % (i,num))
        print("list",list)
        print(id(list))


if __name__ == "__main__":
    # 创建进程
    p = Process(target=test)
    print(type(p))
    print(p)

    # 启动进程
    p.start()

for i in range(3):
    #print("=========>主进程", i)
    num += 1
    list.append(i)
    print("主进程------>i:%d,num:%d" % (i, num))
    print("2list",list)
    print(id(list))
    time.sleep(0.01)


print("程序结束")
