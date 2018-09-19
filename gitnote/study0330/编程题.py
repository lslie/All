import os
from multiprocessing import Process
import time
import random


# 创建一个银行类，初始化属性：账户金额，方法是存钱方法，取钱方法
# 创建2个进程，各自实现操作账户10次，每次产生一个随机数，判断随机数的奇偶性
# ，如果是奇数取钱，否则存钱。完成后打印账户总金额
# 创建银行类
class Bank(object):
    def __init__(self, money):
        super().__init__()
        self.money = money

    # 存钱方法
    def save_money(self, money):
        for i in range(10):
            num = random.randint(0, 100)
            if num % 2 == 0:
                self.money += money
                print("存了%d元,当前余额:%d元,当前进程:%s" % (money, self.money,os.getpid()))
            else:
                bank.get_money(1000)

    # 取钱方法
    def get_money(self, money):
        if money > self.money:
            print("余额不足")
        else:
            self.money -= money
            print("取了%d元,现余额:%d" % (money, self.money))


if __name__ == "__main__":
    bank = Bank(10000)
    save = int(input("请输入存的钱数:"))
    get = int(input("请输入取的钱数:"))
    g = Process(target=bank.save_money, args=(save,))
    p = Process(target=bank.get_money, args=(get,))

    g.start()
    g.join()
    time.sleep(1)
    print("完成操作")
