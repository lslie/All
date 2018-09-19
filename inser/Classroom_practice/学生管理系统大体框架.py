#提示名片打印信息
print("="*50)
print("    名片管理系统1.0")
print('    1.增加一个新的名片')
print("    2.删除一个名片")
print('    3.修改一个名片')
print("    4.查找一个名片")
print('='*50)


#得到用户输入的选项
name=[]
while True:
    num=int(input("请输入您的选择编号："))


    #得到用户的选择，做出相应的处理

    if num ==1:
        new_name=input('请输入新名片的名称')
        name.append(new_name)
        print(new_name)
        print("添加成功")
    elif num==2:
        de_name=input("请输入您要删除的名片的名称")
        if de_name not in name:
            print('删除失败！找不到您输入的信息')
            continue
        else:
            de_index=name.index(de_name)
            del name[de_index]
            print("删除成功")
    elif num==3:
        replace_name=input("请输入您要替换的名片信息：")
        if replace_name not in name:
            print("您输入的信息不正确请重新输入")
            continue
        else:
            replace_index=name.index(replace_name)
            print('{0[replace_index]}'.format(name))
            print('修改成功')
    elif num ==4:
        find_name=input("请输入您要查找的名片信息")
        print(find_name)
    elif num==5:
        break
    else:
        print('您输入有误请重新输入：')
