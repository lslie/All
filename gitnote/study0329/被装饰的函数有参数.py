from time import ctime,sleep
def func(func_name):#将test函数作为参数传入进来
	def inner_func(a,b):#对应的也要传参数
		print("%s in %s gone"%(func_name.__name__,ctime()))
		func_name(a,b)		#变相执行test函数
	return inner_func


@func

def test(a,b):
	sleep(2)
	print('test')
	print(a+b)

test(10,20)