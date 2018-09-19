
def fibs(length):
	a,b=0,1
	n=0
	while n<length:
		a,b=b,a+b
		# yield b
		print(b)
		n+=1


def fib():
	try:
		while True:
			next(f)

	except Exception as result:
		print(result)

f=fibs(20)

f = fib()

