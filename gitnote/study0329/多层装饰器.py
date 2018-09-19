def make_b(func):
	def fun_in():
		result = "<b>" + func() + "</b>"
		return result
	return fun_in


def make_i(func):
	def fun_in():
		result="<i>" + func() + "</i>"
		return result
	return fun_in


@make_b
def test():
	result="hello world"
	return result


@make_i
def test1():
	result="hello world1"
	return result
@make_b
@make_i
def test3():
	result = "hello test3"
	return result


print(test())
print(test1())
print(test3())
