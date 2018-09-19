class Text(object):
    def __init__(self,num):
        super(Text,self).__init__()
        self.num=num


    def abc(self,a,b):
        try:
            num=a/b
            print(num)
        except Exception as a:
            if self.num:
                print("打印异常==%s",a)
            else:
                raise a
        else:
            print("程序正常结束")


Text(False).abc(10,0)
