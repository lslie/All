#定义学生类
class Student(object):
    def run(self):
        print('跑步')
    def eat(self,name):
        print('%s吃东西'%name)
class Copy(Student):
    def eat(self):
        print('吃饭')
#实例化类
stu1=Student()
stu1.eat('张三')
stu2=Copy()
stu2.run()
