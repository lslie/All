#创建三个空列表接收a,b,i的值
list=[]
list1=[]
list3=[]

for i in range(50):
	a = 3692.35 * i ** 0.75
	b = 1147 * (7.21 - i)
	while a - b == 0.5:

		#当a-b<20时讲a,b,i分别添加进list1,2列表
		list.append(a)
		list1.append(b)
		list3.append(i)
		#循环遍历列表得到的就是a,b,i的值
		for x in list:
			print("---->a",x)

		for z in list1:
			print("----->b",z)

		for s in list3:
			print("--->i",s)
		print(i,a,b)
		break