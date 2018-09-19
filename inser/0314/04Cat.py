ass Cat(object):
    #eat
    def eat(self):
        print('%s吃了很多小鱼'%(self.name))
    #drink
    def drink(self):
        print('%s喝了很多可乐'%(self.name))


Tom=Cat()
Tom.name='汤姆猫'
Tom.eat()
Tom.drink()



#创建第二个对象
lanmao=Cat()
lanmao.name='lanmao'
lanmao.eat()
