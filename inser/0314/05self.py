#定义一个学生类，初始化给Name，age赋值，方法：study(专业)
#play_ball(ball)
#定义两个对象stu1stu2对象调用方法
class Student():
    #定义初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=20
    #定义方法专业study
    def study(self,classmate):
        print("%s今年%s岁了，正在学习%s专业"%(self.name,self.age,classmate))
    def play_ball(self,play):
        print("%s正在进行%s活动"%(self.name,play))


stu1=Student('张三',20)
stu1.age=40
stu1.study('python')
stu1.play_ball('打篮球')
print (id(stu1))


stu2=Student('李四',60)
stu2.study('C++')
stu2.play_ball("下象棋")
print(id(stu2))
