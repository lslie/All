#快速完成y=x+1和y=2x+1
#通过闭包
def test(a,b):
	def inner_test(n):
		result=a*n+b
		return result
	return inner_test



#调用完成
func = test(5,1)
print(func(1))
func(2)
func(3)
