def first_test(fun):
	print("我是没装修的房子")

	def second_test():
		print("加点东西")
		fun()
	return second_test

@first_test
def ss():
	print("装修好了")


ss()
