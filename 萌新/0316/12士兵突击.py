#-*-coding:utf-8-*-
'''
许三多：对象
'''
#新建士兵
class Soldier(object):
    #属性
    def __init__(self):
        self.name="姓名"
        self.gun="枪"

    #定义开火
    def fire(self):
        print("士兵可以开火")
    #定义许三多
    def xu_san(self):
        self.name="许三多"
        print(self.name)
#定义枪
class Gun(Soldier):
    '''属性：当前子弹数量，最大数量
	ak47：对象
	发射子弹()  —》数量减少
	装子弹()  —》数量增多'''
    def __init__(self):
        self.bullet_quantity=int(0)  #当前子弹数量
        self.big_bullet=int(30)       #最大数量
    def AK_47(self):
        gun.fire_bullet()
    #定义发射子弹
    def fire_bullet(self):
        while self.bullet_quantity<=int(30) and self.bullet_quantity>=int(0):
            #self.big_bullet
            self.bullet_quantity-=self.bullet_quantity
            #for i in self.bullet_quantity :
            #    print (i)
            while self.bullet_quantity<=int(30):
                self.bullet_quantity-=0
                print(self.bullet_quantity)
                break
            print("没子弹了")
            if self.bullet_quantity==int(0):
                print("正在发射子弹，子弹打完了装弹！")
                Gun.shot_bullet(self)
                break
    #定义装填子弹
    def  shot_bullet(self):
        while self.bullet_quantity==int(0) and self.bullet_quantity>=int(30):
            self.bullet_quantity+=self.bullet_quantity
            while self.bullet_quantity<=int(0):
                self.bullet_quantity+=int(30)
                print(self.bullet_quantity)
                break
            print("正在装弹")
            if self.bullet_quantity==int(30):
                print("子弹装点完毕")
                break

    #士兵突击
class Soldier_assault(object):
    def xu(self):
        #士兵许三多有一把AK47
        soldier.xu_san()
        #士兵可以开火
        soldier.fire()
        #枪能够发射子弹
        gun.AK_47()
        #枪装填子弹，增加子弹数量
soldier=Soldier()  #实例化士兵
#soldier.fire()
#soldier.xu_san()
gun=Gun()
#gun.AK_47()
         #实例化枪
soldier_assault=Soldier_assault() #士兵突击！
soldier_assault.xu()