#3.创建一个车类，提供属性：颜色，速度。方法：移动()。停止()。  创建两个子类：自行车，跑车。分    别新增属性和方法。创建对象，进行测试。



class Car(object):
    color="红色"
    speed=170

    #定义移动
    def move(self):
        print('车能快速移动')



    #定义停止
    def tingzhi(self):
        print("刹车不错")


#创建自行车
class One_car(Car):
    name = "自行车"
    def zixingche(self):
        print("自行车也能骑很快")




#创建跑车
class Run_car(Car):
    name="跑车"
    def paoche(self):
        print("跑车很厉害")



car=Car()
car.move()
car.tingzhi()
print('--------自行车')
zixingche=One_car()
print(zixingche.name)
zixingche.zixingche()
print('---------跑车')
paoche=Run_car()
print(paoche.name)
paoche.paoche()
