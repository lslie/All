#第1题，写一个闭包，内部函数里面调用外部函数的命名空间的变量(包括形参，和局部变量),
# 分析执行原理，并说明闭包的优缺点（20分）
d=10							#全局变量
def test(a,b):
	c=20						#函数test的局部变量
	print("------>first")
	def inner_test():			#定义内嵌函数inner_test
		nonlocal c				#因为此处要改变c的值所以申明此处的c不是Inner_test的变量
		c=a+b+c+d
		print(c)

	return inner_test			#返回内嵌函数


f=test(2,6)
f()
