#第3题 写一个装饰器案例被装饰的函数有参数（有缺省参数和不定长参数）有返回值。（20分
#定义装饰器

def decorator(fun):
	print("装饰器第一层")

	def inner_decorator(*args,sex=10,**kwargs):
		print(sex,args,kwargs)

		for i in args:
			i=i.split('?')
			print(i)
			i=i[1].split("&")
			for x in i:
				x=x.split("=")
				print(x)
				# print(x)
		print("分解完毕")
		for v in kwargs.keys():
			print("名字是%s"%v)
		for x in kwargs.values():
			print("性别是%s"%x)
		print("年龄是%s" %sex)
		fun()
	return inner_decorator
@decorator
#定义函数执行
def carry_out(sex=10,*args,**kwargs):
	print("by_whilteK")


name=(input("请输入要分解的网址:"))
new_name=input("请输入您的名字:")
sex=input("请输入您的性别")
dicts={new_name:sex}
carry_out(name,**dicts)
#https://www.baidu.com/baidu?isource=infinity&iname=baidu&itype=web&tn=98012088_6_dg&ch=13&ie=utf-8&wd=baidu