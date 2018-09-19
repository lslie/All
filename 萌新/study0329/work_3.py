#使用type创建一个类，
# 并且给类添加类属性和实例方法、静态方法、类方法。
#创建person类
Person=type('Person',(object,),{})

#添加类方法
@classmethod
def test(cls):
	print("类方法")
	return 'Dome'
#添加静态方法
@staticmethod
def test1():
	print("静态方法")
	return 'Dome' 
def test3():
	print("实例方法")
	return 'DOMe'
#添加属性跟方法
Person.name='张三'
Person.test=test
Person.test1=test1
person=Person()
person.test3=test3
#调用属性方法
print(Person.name)
print(Person.test())
print(Person.test1())
print(person.test3())
