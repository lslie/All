import time
from multiprocessing import Process
#join加入/插队
num = 100
list=[0,2]


def test():
    print("我是test方法")
    for i in range(3):

        print("子进程------>i:%d,num:%d" % (i,num))
        print("list",list)
        time.sleep(0.3)
    print('子进程listID:', id(list))


if __name__ == "__main__":
    # 创建进程
    p = Process(target=test)
    print(type(p))
    print(p)

    # 启动进程
    p.start()
    #join  让你的主进程让步
    p.join(1)#主进程让给子进程1S时间
    if p.is_alive():#判断程序是否存活
        print("还有人活着")
        p.terminate()#不管你执行完没有强制kill
    else:
        print("已经没有生口了")

for i in range(3):
    #print("=========>主进程", i)
    num += 1
    list.append(i)
    print("主进程------>i:%d,num:%d" % (i, num))
    print("2list",list)
    print(id(list))
    time.sleep(0.01)


print("程序结束")