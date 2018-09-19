def test(num):
	a=5
	b=8
	print("outer--------->1")
	def inner_test(x):
		str=0
		s = [x for x in range(x)]
		for i in s:
			print(i)
			while i<100:
				str+=i
				i+=1

			print(str)

		print("inner------------>1")
		result=a+b+num
		print("inner-------->2")
		print(result)
	return inner_test

fun=test(1)
fun(100)