'''
1.西游记:3个徒弟
	类：父类：唐僧的徒弟
		属性： name，age，
                方法： 吃饭，取经，
	子类：
	 孙悟空：属性： name，age，武器，  方法： 吃饭，取经，除妖。。。
        定义对象测试
'''
#定义父类唐僧
class Tang_seng(object):
    name="唐僧"
    __age=1000
    #定义吃饭方法
    def eat(self):
        print("师傅只吃米饭")
    #定义取经方法
    def go_q(self):
        print("%s今日启程了"%(self.name))
    #设置年龄为私有属性
    def set_age(self,age):
        if age<1000:
            print("太小了我不接受我最起码也是师傅啊")
        else:
            self.__age=age
    def get_age(self):
        return "%s今年%s岁了"%(self.name,self.__age)

#定义子类猴子
class Hou_zi(Tang_seng):
    name="猴子"
    age=1800
    weapon="金箍棒"   #武器
    #定义吃饭方法
    def eat(self):
        print("大师兄只吃桃")
    #定义取经方法
    def go_q(self):
        print("是师傅的大徒弟")
    #定义除妖方法
    def device(self):
        print("大师兄一路上我除掉了大部分妖怪")


#定义子类猪八戒：属性： name，age，字符串媳妇，   方法：吃饭，取经，牵马。。
class Zhu_bajie(Tang_seng):
    name="猪八戒"
    age=1600
    wife="高翠兰"
    #吃饭
    def eat(self):
        print("我最能吃！")
        super().eat()
        Hou_zi.eat(self)
        Sha_wujing.eat(self)        
    #取经
    def go_q(self,monster):
        print("我是二徒弟%s是我的大师兄，%s是我的三师弟"%(Hou_zi.name,Sha_wujing.name))#使用类.对象名
        #妖怪个数
        if len(monster)<=0:
            print("别把%s至少杀了一只老虎啊！"%(Hou_zi.name))
        else:
            print("这一路上我杀了下面这么多妖怪：")
            for x in monster:
                print(x)
        print("="*50)
    #牵马
    def lead(self):
        Hou_zi.device(self)
        print("我的任务是牵马")
        Sha_wujing.pick(self)

#定义自雷沙和尚：属性： name，age，流沙河，   方法： 吃饭，取经，挑行李。。。
class Sha_wujing(Tang_seng):
    name="沙和尚"
    age=1600
    address="流沙河"
    #吃饭
    def eat(self):
        print("沙师弟有点呆吃的不多。。。")
    #取经
    def go_q(self):
        print("我是三徒弟")
    #挑行礼
    def pick(self):
        print("沙师弟的任务是挑行礼！")
tangseng=Tang_seng()
houzi=Hou_zi()
shawujing=Sha_wujing()
tangseng.go_q()         #取经开始
houzi.go_q()
zhubajie=Zhu_bajie()
zhubajie.eat()
monster=('老虎','白骨精','红孩儿','牛魔王','铁扇公主','等')
zhubajie.go_q(monster)
shawujing.go_q()
print('-----------年龄---------')
tangseng.set_age(1500)
age=tangseng.get_age()
print(age)
print("%s今年%s岁了"%(houzi.name,houzi.age))
print("%s今年%s岁了"%(zhubajie.name,zhubajie.age))
print("%s今年%s岁了"%(shawujing.name,shawujing.age))
print('------------任务-----------')
zhubajie.lead()
