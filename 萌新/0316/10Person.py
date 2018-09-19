#4.创建Person类。属性：姓名，私有年龄。方法：显示信息和设置私有年龄的set和get方法
# 创建两个子类：学生和工人。  分别新增属性成绩和工资。   
# 创建对象测试
class Person(object):
    name="张三"
    __age=0
    def set_age(self,age):
        self.__age=age

    def get_age(self):
        return self.__age


    def __str__(self):
        msg="姓名："+Person.name+"年龄"+str(self.get_age())
        return msg



class Student(Person):
    grade=100


class Worker(Person):
    salary=1000


print('--------父类person')
person=Person()
person.set_age(50)
age=person.get_age()
print(age)

print('--------学生')
student=Student()
print(student)
print("成绩为%s"%(student.grade))
print('---------工人')
worker=Worker()
print("工资为%s"%(worker.salary))
