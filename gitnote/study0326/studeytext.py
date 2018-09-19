class Text(object):
	def __init__(self,name):
		self._name=name
		self.__age=0
	# @property
	# def age(self):
	# 	return self.__age
	# @age.setter
	# def age(self,age):
	# 	self.__age=age
	def get_age(self):
		return self.__age
	def set_age(self,age):
		self.__age=age
	age=property(get_age,set_age)




name='李白'
age=20
text=Text(name)
text.age=21
print(text.age)
print(text._name)