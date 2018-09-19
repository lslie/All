def func_args(args):
	print("func_args--args",args)

	def func(func_name):
		print('func/....func_name',func_name.__name__)
		def func_in():
			print('func_in--args',args)
			func_name()
		return func_in
	return func

@func_args("atguigu")
def test():
	print('test')

test()