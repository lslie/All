def a():
	print("a")
def b():
	print("b")
def test(func1,func2):
	def test_inner(func):
		def inner_test(*args,**kwargs):
			func1()
			result=func()
			if (result != None):
				return result
			func2()

		return inner_test
	return test_inner
@test(a,b)

def demo():
	print("c")
demo()