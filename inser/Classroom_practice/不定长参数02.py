def dowload_nums(**kwargs):
    if len(kwargs)==0:
        print("输入无效，请重新输入！")
    else:
        for c in kwargs.items():
            print(c)
name=input("请输入您的名字：")
age=int(input("请输入您的年龄："))
dowload_nums("'name':name","'age':age")
