#键盘输入多个人名保存到一个列表中
#如果里面有重复的则提示此姓名已经存在
#print("="*20)
#name=[{'name':'张旭'},{'name':'郑欣'},{'name':'樊杰'}]
#list_name={}
# new_name=input("请输入您要添加的姓名：")
#遍历原列表中的姓名
'''
定义查找添加姓名函数
1、首先循环遍历已知数组name将里面的字典列出来
2、判断输入的名字是否在遍历出来的字典里通过 字典.key=value知识点
3、如果没有就跳出循环执行else
4、将输入的名字添加入新建的容器list_name存放
5、然后将list_name添加进列表Name
6、跳出不然会持续执行
'''
def name_obj():
    for card in name:
        if card['name']==new_name:
            print("您输入的名字已存在请重新输入")
            break
         #   i=1
        #if i==0:
        else:
            list_name['name']=(new_name)
            name.append(list_name)
            print("添加成功")
            break
'''
定义循环执行while Ture
1、输入序号必须是int不然会报错
2、如果输入的是1执行函数new_obj()
3、2直接break
4、其余数字直接报错
'''
while True:
    print('='*50)
    print("1、添加姓名")
    print("2、退出")
    num=int(input("请输入序号："))
    if num==1:
        name=[{'name':'张旭'},{'name':'郑欣'},{'name':'樊杰'}]
        list_name={}
        new_name=str(input("请输入您要添加的姓名："))
        name_obj()
    elif num==2:
        break
    else:
        print("输入错误，请重新输入！")
    print('='*50)
