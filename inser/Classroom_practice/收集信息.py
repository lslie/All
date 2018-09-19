phones=[]    #建立容器
phones_index={}    #建立放手机信息的字典
phone_in=str(input('请输入您要查找的手机名称'))
flag=0
for phone in phones:     #查找手机
    print(phones_index)
    if phone==phone_in:
        flag=1
if flag==0:
    phone_price=input("请输入您的手机价格:")
    phone_red=input("请输入您的手机颜色:")
    phones_index['手机名称']=phone_in
    phones_index['手机价格']=phone_price
    phones_index['手机颜色']=phone_red
    phones.append(phones_index)
    print("没有查到您想要的手机信息，但是您的手机信息已录取")
    print(phones_index)
    print(phones)
