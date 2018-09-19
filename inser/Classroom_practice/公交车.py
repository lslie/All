bus_car=int(input("请输入您的卡内余额："))
if bus_car>2:
    print("上车")
    bus_seat=int(input("请输入您看到车上有几个空座位"))
    if bus_seat>0:
        print("可以做哦")
    else:
        print("站是一种美德")
else:
    print("get out!")
