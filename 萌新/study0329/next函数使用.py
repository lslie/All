def gen():
	i= 0
	while i < 5:
		temp= yield i
		print('---->temp',temp)
		i+=1


f=gen()
print(f.__next__())
print(f.__next__())