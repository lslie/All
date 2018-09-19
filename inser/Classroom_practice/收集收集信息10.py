phone=[{'name':'小木','price':2000}]
phone_new=input('请输入您想查找的收集型号')
i=0
length=len(phone)
while i<length:
    phone_l=phone[i]
    if phone_l.get("name")==phone_new:
        print('存在')
        braek
    i=i+1
if i==length:
    new_phone={}
    new_phone['name']=phone_new
    phone.append(new_phone)
    print(phone)
