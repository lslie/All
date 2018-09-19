try:

	list_=[]

	f=open("text.txt","r")
	a=f.readlines()
	print(a)
	for x in a:
		dic = {}
		x=x.split()
		#print(x)
		dic["name"]=x[0]
		dic["sex"]=x[2]
		dic["age"]=x[1]
		#value=dic["sex"].values()
		#print(value)
		#print(dic)
		list_.append(dic)
		print(list_)
	f.close()

except FileNotFoundError:
	print("文件不存在")

except:
	print("出现其他错误")
finally:

	print("执行完毕")