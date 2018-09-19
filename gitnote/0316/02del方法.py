import time
class Person(object):
	def __init__(self,name):
		print("方法被调用")
		self.name = name
	def peint_info(self):
		print(self.name)
	def __del__(self):
		print("Person即将销毁")
		print("%s对象马上被干掉了。。。"%self.name)

t=Person("张三")
t.peint_info()
del t
print('-------')
cat = Person("波斯猫")
cat2=cat
cat3=cat
print('马上删cat对象')
del cat
print('马上删cat2对象')
del cat2
print('马上删cat3对象')
del cat3
print("程序两秒后结束")
time.sleep(2)
