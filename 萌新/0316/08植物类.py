#2.创建父类植物类，属性：名称。方法：显示属性信息。创建两个子类：
#  花和草。分别新增属性和功能。   创建对象测试
#创建父类植物类
class Botany(object):
    name="植物"
    __age=90
    def set_age(self,age):
        if age>100 and age<50:
            self.__age=age
        else:
            print("你把我说的太老了")
    def get_age(self):
        return self.__age

#创建花
class Flower(Botany):



    def color(self):
        print("我的颜色真好看")
#创建草
class Grass(Botany):



    def grenn(self):
        print("我的颜色是绿色的！")
    def str(self):
        Grass.name="小绿"
        print("我的名字是%s"%(self.name))
        self.grenn()



botany=Botany()
botany.set_age(80)
age=botany.get_age()
print("%s今年%s百年了"%(botany.name,age))

print('--------花----------')
flower=Flower()
flower.name="小红"
flower.color()
print(flower.name)
print("---------草---------")
grass=Grass()
grass.str()
