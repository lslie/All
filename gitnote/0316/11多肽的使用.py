#-*-coding:utf-8-*-
#.多态的使用
#  有三种动物：狗、猫、猪，
#	父类：动物、
#	子类：狗、猫、猪   可以添加子类自己的方法，自己扩展
#	动物的属性：动物的名字
#	动物的方法是eat（就是打印自己的名字）
#   有一个饲养员：饲养员
#	饲养员的方法：feed_animal(需要饲养的动物)
#		函数的实现是（其实就是调用动物的eat方法）
class Animal(object):
    name="动物"
    def eat(self):
        print("%s会吃东西"%(self.name))
class Dog(Animal):
    def eat(self):
        print("小狗吃骨头")

class Cat(Animal):
    def eat(self):
        print("小猫爱吃鱼")

class Pig(Animal):
    def eat(self):
        print("小猪不知道吃什么")


class Breeder(object):
    def feed_animal(self,animal):
        animal.eat()        

breeder=Breeder()
dog=Dog()
breeder.feed_animal(dog)
cat=Cat()
breeder.feed_animal(cat)
pig=Pig()
breeder.feed_animal(pig)
