class Animal(object):
    def work(self):
        print("我出去工作了。。。。。")
class Guanli(Animal):
    def work(self,womens):
        super().work()
        print("管理这些人：")
        for x in womens:
            print(x)
        Come_back.work(self)
class Come_back(Guanli):
    def work(self):
        print("下班了我回来了。。。。")
women=Guanli()
womens=('小明','郑欣','范姐')
women.work(womens)
