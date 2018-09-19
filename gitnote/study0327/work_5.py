#写一个闭包案例，并且说明你对闭包的理解
def text():
	a=10
	b=20
	def inner_text():
		num=a+b
		print(num)
		return "你好"
	return inner_text


a=text()
print(a())

