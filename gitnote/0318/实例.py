class Home(object):
    __int=None


    def __new__(cls):
        if cls.__int==None:
            cls.__int=object.__new__(cls)
            return cls.__int
        else:
            return cls.__int


    def __init__(self):
        pass


a=Home()
b=Home()
print(id(a))
print(id(b))
