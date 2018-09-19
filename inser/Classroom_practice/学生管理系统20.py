print("="*50)
print("\t名片管理系统1.0")
print("\t1.增加一个新名片")
print("\t2.删除一个名片")
print("\t3.修改一个名片")
print("\t4.查找一个名片")
print("\t5.退出名片管理系统")
print("="*50)

card_info=[{'name':'小明','sex':'男','age':'18','ads':'尚硅谷'}]
i=1
while True:
    print("请输入您选择的编号:")
    number=int(input("请输入对应的编号进行操作（1~5）:"))
    if number==1:
	#增加一个新名片
        new_name={}
        name=print(input("请输入您的性名："))
        sex=print(input("请输入您的性别："))
        age=print(input("请输入您的年龄："))
        ads=print(input("请输入您的联系地址"))
        new_name['name']=name
        new_name['sex']=sex
        new_name['age']=age
        new_name['ads']=ads
        car_info.append(new_name)        
        print(card_info)
    elif number==2:
	#删除一个名片  
        dell_name=print(input("请输入您要删除的姓名："))
        for card in card_info:
            card_bard=card.get('dell_name')
            if card_bard==dell_name:
                del card
                card_bard.remove(card)
                print("card_info")
                print("删除成功")
    elif number==3:
	#修改一个名片
        alter={}
        update_name=print(input("请输入您想修改的姓名："))
        for update in card_info:
            updatecard=update.get("update_name")
            if updatecard==update_name:
                del card
                card_bard.remove(card)
                print("请输入您要修改的信息：")
                alter_name=print(input("请输入您修改的名字："))
                alter_sex=print(input("请输入您要修改的性别："))
                alter_age=print(input("请输入您要修改的年龄："))
                alter_ads=print(input("请输入您要修改的地址："))
                alter['name']=alter_name
                alter['sex']=alter_sex
                alter['age']=alter_age
                alter['ads']=alter_ads
                card_info.append(alter)
                print(card_info)
    elif number==4:
        #查找一个名片
        find_name=print(input("请输入您要查找的名片信息："))
        for find in card_info:
            findname=find.git("find_name")
            if findname==find_name:
                print(find)
    elif number==5:
    	break

