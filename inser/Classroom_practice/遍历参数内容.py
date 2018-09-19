def text1(**kwargs):    #定义函数用来遍历字典内容
    if len(kwargs)==0:   #判断参数是否为空
        print("输入有误")
    else:                #如果参数不是空值就遍历出他的值
        for x in kwargs.items():
            print(x)
def text2(**kwargs):
    text1(**kwargs)
    if new_name==kwargs['name']:
        kwargs['name']=new_name
        print(kwargs)
new_name=input("请输入您的名字：")
new_age=int(input("请输入您的年龄："))
new_sex=input("请输入您的性别：")
text2(name=new_name,age=new_age,sex=new_age)
