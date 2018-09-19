class Student(object):
    def __init__(self, name):
        self.name = name
        self.age = 20
        self.sex = '男'
    #定义限制属性方法
    def __getattribute__(self, obj):
        print("执行getattribute")
        #判断调用了那个方法
        if obj == 'name':
            print("name")
            #返回这个实例的属性的值
            return object.__getattribute__(self,obj)
        elif obj == 'age':
            print("age")
            return object.__getattribute__(self, obj)
        else:
            print("其他")
            return object.__getattribute__(self, obj)


student = Student('张三')
print(student.name)
print(student.age)
print(student.sex)
