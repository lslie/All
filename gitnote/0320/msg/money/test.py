num="我是全局变量"
def inst():
    print("我是函数")

class Next(object):
    def __init__(self):
        print("我是一个函数")
if __name__=="__main__":
    print(num)
    inst()
    a=Next()
    print(a)
