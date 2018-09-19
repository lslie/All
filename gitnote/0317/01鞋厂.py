'''3定义一个类（），类跟工厂关联的
- 鞋厂（Shoe）
- 皮鞋，运动鞋妥协
- 鞋的工厂类ShoeFactory---->专卖店：'''


#定义鞋厂
class Shoe(object):
    def __init__(self):
        pass
    def __make_show(self,type_shoe):
        Shoe_work.shoe_work_type(self,type_shoe)
class Tuo_xie(Shoe):
    def __init__(self):
        self.name="拖鞋"
class Pi_xie(Shoe):
    def __init__(self):
        self.name="皮鞋"



#定义鞋子类
class Shoe_work:
    def shoe_work_type(self,work):
        if work=="拖鞋":
            return Tuo_xie()
        elif work=="皮鞋":
            return Pi_xie()


#专卖店
class Exclusive_shop(object):
    __tell=Shoe()