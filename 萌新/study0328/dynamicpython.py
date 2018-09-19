# class Test(object):
# 	pass
# t=Test()
# print(t)
# Test2 = type("Test2",(object,),{"color":"银色"})
# t2 = Test2
# s=Test2.color
# print(s)
# print(type(t2))
# print(help(t2))
#
#
#
# Test3=type("IPhone",(Test2,),{"brand":"苹果"})
#
#
# print(help(Test3))



class Phone(object):
	color="银色"


Phone.brand='OPPO'
Phone.price=1999

class IPhone(Phone):
	brand="苹果"
