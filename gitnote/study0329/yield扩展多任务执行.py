def test():
	while True:
		print('--------1---------')
		yield None


def test1():
	while True:
		print('--------2----------')
		yield None


t1 = test()
t2 = test1()

while True:
	t1.__next__()
	t2.__next__()
