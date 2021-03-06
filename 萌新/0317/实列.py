class Singleton(object):

    __instance=None
    __first_init=False


    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance
    def __init__(self,age,name):
        if not self.__first_init:
            self.age=age
            self.name=name
            Singleton.__first_init=True



a=Singleton(18,'dongge')
print(id(a))
b=Singleton(18,'dongge')
print(id(b))
print(a.age)
print(b.age)
a.age=19
print(b.age)