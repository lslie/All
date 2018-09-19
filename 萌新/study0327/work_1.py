#第2题 写一个装饰器给某个函数统计该函数的执行时间分析执行原理，说明装饰器的好处。（10分）
import time
#定义装饰器
def time_decorator(fun):
	print("正在验证....")
	def decorator():
		start_=time.time()
		fun()
		end_=time.time()
		num=end_-start_
		print("验证使用了%s" % num)
	return decorator
@time_decorator
# 定义函数执行装饰器
def func():
	print("验证完了")

func()



'''装饰器的依赖是闭包,当Python解释器遇到@xxx的时候
自动将@xxx下面的函数当做参数传入time_decorator()中
,自动执行print("正在验证")随后顺序执行 decorator函数
start_获取当前时间
fun()执行func()函数
end_表示执行完func函数的时间
num表示end于start之间相差
随后打印num的值
然后返回内嵌函数
执行func()
执行内嵌函数
装饰器是在不改变原有函数代码块的同时优化增加函数的功能
'''
