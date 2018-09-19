class People(object):
    __intt=None


    def __new__(cls):
        if cls.__intt==None:
            cls.__intt=object.__new__(cls)
            return cls.__init
        else:
            return cls.__intt




a=People()
b=People()
print(id(a))
print(id(b))
