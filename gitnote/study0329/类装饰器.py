class Test():
	def __init__(self,fun):
		print("初始化")
		self.__fun=fun

	def funcc(self):
		print('方法')
		#self.__fun()


	def __call__(self):
		print('call me')
		self.__fun()


@Test
def test():
	print("test-------")

test()
test.funcc()