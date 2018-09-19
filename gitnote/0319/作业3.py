#写一个程序，里面包含捕获异常所有的语法
class ShortInputException(Exception):

    def __init__(self,length,atlrast):
        super(ShortInputException).__init__()
        self.length=length
        self.atlrast=atlrast

    try:
        s=input("请输入用户名不得少于6个字")
        if len(s)<6:
            raise ShortInputException(len(s),6)
    except EOFError:
        print("你输入了一个结束标记EOF")

    except ShortInputException as result:
        print("ShortInputException：输入的长度是%d,用户名至少应该是%d"%(result.length,result.atleast))


    else:
        print("没有异常发生")
    finally:
        print ("我必须要出现")
