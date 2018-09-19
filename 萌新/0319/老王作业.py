#-*-coding:utf-8-*-
class Person(object):

    def __init__(self, name):
        super(Person, self).__init__()
        # object.__init__(cls)
        self.name = name
        self.gun = None
        self.hp = 100  # 血量  默认值100

    def anzhuang_zidan(self, zidan_temp, danjia_temp):
        danjia_temp.baocun_zidan(zidan_temp)

    # 人负责给枪安装弹夹
    def anzhuang_danjia(self, gun, danjia_temp):
        gun.anzhuang_danjia(danjia_temp)

    # 拿枪
    def naqiang(self, gun_temp):
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return "%s有枪，生命值是:%d" % (self.name, self.hp)
        else:
            return "%s没有枪，生命值是:%d" % (self.name, self.hp)

    # 定义一个开枪动作
    def kaiqiang(self, enmey):
        if enmey.hp == 0:
            print("%s血量为0,不要浪费子弹了..." % (enmey.name))
        else:
            self.gun.fire(enmey)

    # 掉血
    def diaoxue(self, sha_shang_li):
        if self.hp <= sha_shang_li:
            self.hp = 0
            print("血量为0，游戏结束....")
        else:
            self.hp -= sha_shang_li


class Gun(object):
    """枪类"""

    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.danjia = None  # 默认没有弹夹

    # 安装弹夹
    def anzhuang_danjia(self, danjia_temp):
        self.danjia = danjia_temp

    # 枪定义一个开火动作
    def fire(self, enmey):
        # 弹出子弹
        zidan = self.danjia.tanchu_zidan()
        if zidan == None:
            print("没有子弹")
        else:
            # 射击敌人
            zidan.sheji(enmey)


class Danjia(object):
    """弹夹类"""

    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num  # 最多装20发子弹
        self.zidan_list = []

    def baocun_zidan(self, zidan_temp):
        self.zidan_list.append(zidan_temp)

    def tanchu_zidan(self):
        if len(self.zidan_list) == 0:
            return None
        else:
            return self.zidan_list.pop()


class Zidan(object):
    """子弹类"""

    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li

    def sheji(self, enmey):
        enmey.diaoxue(self.sha_shang_li)


def main():
    # 搭建框架

    # 创建4个实例对象

    # 创建老王实例
    laowang = Person("老王")

    # 创建枪实例
    gun = Gun("AK47")

    # 创建弹夹
    danjia = Danjia(20)

    # 创建多个子弹实例
    for i in range(20):
        zidan = Zidan(10)

        # 老王装子弹到弹夹
        laowang.anzhuang_zidan(zidan, danjia)

    # 装弹夹到枪
    laowang.anzhuang_danjia(gun, danjia)

    # 老王保存枪
    laowang.naqiang(gun)
    print(laowang)
    # 创建一个敌人对象
    laosong = Person("老宋")
    print(laosong)
    # 开枪打敌人
    for i in range(20):
        if laosong.hp <= 0:
            break
        else:
            laowang.kaiqiang(laosong)
            print(laosong)


# 程序默认的__name__的值就是__main__
# __name__如果在当前类中使用的话，则值__main__
# 如果是当前类导入到其他类中，再去查看Homework的__name__,打印的就是类名
# 记住：在当前类中使用：__name__=="__main__"

if __name__ == "__main__":  # 判断是否是当前类

    main()
    print("==================")