def text(fun):
	print("开始装修")

	def innter_text():
		print("加点装饰")
		fun()

	return innter_text


@text
def abc():
	print("装修完毕")

abc()