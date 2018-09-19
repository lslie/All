class Animal(object):
    name="动物"
    sort="哺乳类"
    sex="母的"
    age=1
    def eat(self):
        print("%s，他的性别是%s,今年%s岁了"%(Animal.name,self.sex,Animal.age))

class Cat(Animal):
    pass
class Dog(Animal):
    pass
class Brid(Animal):
    def __init__(self):
        print("我是一直小鸟")
    def fly(self):
        print("%s小鸟在高高的飞翔...."%(self.name))

cat=Cat()
cat.eat()
dog=Dog()
dog.sex="男的"
dog.eat()
brid=Brid()
brid.name="花花"
brid.fly()
