from time import ctime
#装饰器
def check_login(fun):

	def inner_check():
		flag = 0
		# nonlocal name
		# nonlocal login
		name=input("请输入用户名")
		login=input("请输入密码")
		if name=='张三' and login == '123456':
			print("登录成功",ctime())
			flag=1
		if flag==0:
			print("登录失败请重新登录",ctime())
		print("验证2")
		print("验证3")
		fun()
	return inner_check

@check_login
def f1():
	print('数据操作')

@check_login
def f2():
	print('redis调用')

@check_login
def f3():
	print('监控API')

@check_login
def f4():
	print("基础功能")



f1()




