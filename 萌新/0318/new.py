class Text(object):
    def __init__(self):
        print("-------这是Init方法")
    def __str__(self):
        return "这是str方法"
    def __del__(self):
        print("---这是del方法")


    def __new__(cls):
        print("执行new方法")
        return object.__new__(cls)



a=Text()
print(a)
