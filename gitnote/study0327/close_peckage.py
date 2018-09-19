#创建一个闭包返回一个内置函数
def test():
	a=1
	b=2
	def test1():
		print(a+b)
	return test1

f=test()
a=f()
print(a)