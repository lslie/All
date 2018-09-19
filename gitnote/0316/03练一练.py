class Person():
    def __money1(self):
        print("私有属性__money:%s"%(Person.__money))
    def money(self):
        self.__money="保密"
        print("普通方法test")
        self.__money1()
t=Person()
t.money()
