import hashlib


class LoginSys(object):
	# 加密
	def str_md5(self, password):
		m = hashlib.md5()
		m.update(password.encode("utf-8"))
		return m.hexdigest()


	def main(self):
		f=open("password.txt","a+")
		f.seek(0,0)
		#读取所有内容
		content=f.read()

		#判断内容长度
		if len(content)<=0:
			#注册
			print("请根据提示输入内容:")
			name=input("输入用户名:")
			password=input("输入密码:")

			fw=open("password.txt","w+")
			#写入用户
			fw.write(name)
			fw.write("\n")
			#写入密码
			fw.write(self.str_md5(password))

			#关闭流
			fw.close()

		else:
			#登录
			print("欢迎用户登录")
			name=input("输入用户名:")
			password=input("输入密码:")


			fr=open("password.txt","r+")

			file_name=fr.readline()

			print("文件中名字:",len(file_name))
			print("输入的名字:",len(name))

			if file_name.strip()==name.strip():
				#名字正确的话再去读取密码
				file_password=fr.readline()

				md5_password=self.str_md5(password)

				#比较密码
				if file_password==md5_password:
					print("用户登录成功!")
				else:
					print("密码输入有误!")


			else:
				print("用户名输入有误!")


#创建对象

loginSystem=LoginSys()

loginSystem.main()
