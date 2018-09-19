class NameError(Exception):
    def __init(self,num,msg):
        super(NameError,self).__init__()
        self.num=num
        selg.msg=msg


class Text(object):
    def start (self):
        try:
            content=input("请输入内容：")
            if len(content)<3:
                raise NameError(len(content),3)
        except NameError as a:
            print("当前长度是：%d.至少输入长度%d"%(a.length,s.atleast))



t=Text()
t.start()
