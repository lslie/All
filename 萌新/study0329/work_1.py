import types
#创建一个Person类，
# 在该类对象中添加类属性和类方法，
# 然后调用方法。
# 给对象动态添加有参数的方法，然后调用方法，
# 创建对象后用对象调用添加的类属性和类方法。

#创建有参数的方法
def num(*args):
	for i in args:
		print (i)
#创建Person类
Person=type("Person",(object,),{})
#创建函数eat
@classmethod
def eat(cls):
	print("方法吃东西")

#给类添加属性
Person.name="小花猫"
#添加类方法
Person.eat=eat
#调用方法
Person.eat()
#创建对象
p=Person()
#添加有参数的方法
p.num=types.MethodType(num,p)
p.num(*[1,2,3,4])
#调用类属性
print(p.name)
#调用类方法
p.eat()
print(dir(p))