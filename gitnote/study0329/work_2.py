#用__slots__指定添加对象属性和对象方法
class Student(object):
	__slots__ = ["_name","age","get_name"]

def get_name(self):
	print(self._name)
def ss():
	print("测试")
student=Student()
#添加对象属性
student._name='张三'
student.age=19
#添加对象方法
student.get_name=get_name(student)
#执行对象方法或者属性
print(student._name)
print(student.age)
print(dir(student))
