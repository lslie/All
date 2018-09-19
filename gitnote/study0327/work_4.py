#第4题 请用两种方式实现一个生成器，并且使用三种方式取出值（10分）
def text(num):
	a,b=0,1
	n=0
	while n<num:
		print(b)
		temp=yield b
		print(temp)
		a,b=b,(a+b)
		n+=1

a=text(20)
next(a)
next(a)
next(a)
next(a)
a.__next__()
a.send('------?')
a.send(233)
a.send(233)