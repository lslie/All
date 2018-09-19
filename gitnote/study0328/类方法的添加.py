#普通函数
def eat():
	print("吃东西.....")


#函数
def run(self):
	print("奔跑中")

#静态函数
@staticmethod
def show_static():
	print("我是静态函数show")

#类函数
@classmethod
def show_class(cls):
	print("我是类函数show")

Test=type("Test",(object,),{"eat":eat,"run":run,"show_static":show_static,"show_class":show_class})

print(help(Test))

#Test.run()

test=Test()
test.run()
test.show_static()
test.show_class()
Test.eat()
