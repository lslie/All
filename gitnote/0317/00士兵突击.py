#-*-coding:utf-8-*-
"""
1.士兵突击
			1.士兵许三多有一把AK47
			2.士兵可以开火
			3.枪能够发射子弹
			4.枪装填子弹，增加子弹数量

士兵：类
	属性: 可以初始化赋值属性
	   姓名
	   枪
    方法：
      开火()
许三多：对象
枪：类
   属性：当前子弹数量，最大数量
	ak47：对象
	发射子弹()  —》数量减少
	装子弹()  —》数量增多


"""


class Solider:

    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    # 定义开火方法
    def fire(self):
        while True:
            self.gun.shot_bullet()
            # 装子弹
            number = input("请输入子弹的数量:")
            if int(number) == 0:
                break
            else:
                self.gun.load_bullet(int(number))


# 定义枪类

class Gun:
    # 类属性：
    max = 30

    def __init__(self):
        self.current_num = 0

    # 装子弹方法
    def load_bullet(self, number):
        need_num = self.max - self.current_num

        if need_num <= number:
            print("枪装满子弹了....")
            self.current_num = self.max
        elif need_num > number:
            print("子弹还未装满.....")
            self.current_num += number

    # 发射子弹
    def shot_bullet(self):
        while True:
            if self.current_num <= 0:
                print("子弹用光了...,赶快装子弹")
                break

            print("发射第%d颗子弹...." % self.current_num)

            # 子弹就要减少
            self.current_num -= 1


# 创建对象测试

gun = Gun()  # 创建枪

xusanduo = Solider("许三多", gun)

# 开火
xusanduo.fire()







