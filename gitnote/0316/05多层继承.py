class Animal(object):
    def eat(self):
        print("-----吃------")
    def drink(self):
        print("----和------")
    def sleep(self):
        print("----睡觉----")
    def run(self):
        print("----跑-----")
class Dog(Animal):
    def sleep(self):
        print("----睡觉----")
    def run(self):
        print("----跑-----")
    def call(self):
        print("汪汪叫-----")
class Xiaoq(Dog):
    def fly(self):
        print("----飞----")
xtq=Xiaoq()
xtq.fly()
xtq.call()
xtq.eat()
