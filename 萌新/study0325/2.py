class Person(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age=age

	def set_age(self,age):
		self.age=age

	def set_name(self,name):
		self.name = name
	def get_age(self):

		return self.__age
	def get_name(self):
		return self.__name



person=Person('礼拜',20)
age=input('输入你要修改的年龄')
name=input('输入你要修改的名字')
person.set_age(age)
person.set_name(name)
age_new=person.get_age()
age_name=person.get_name()

print("修改后的名字:%s,年龄为%s"%(age_name,age_new))


item_list=[]

for item in range(5):
	print(item)
	item_list.append(person)

for x in item_list:
	print(x.get_name())