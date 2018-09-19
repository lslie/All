def counter():
	print('------1')
	num=10
	def incr():
		print('----------2')
		nonlocal num
		num+=1
		def innerincr():
			print('------------3')
			nonlocal num
			num+=1
			return num
		return innerincr
	return incr


print(counter()()())
print(dir(counter))