#从键盘输入刀子的长度，如果没有超过10cm就能上火车否则不行
knife=int(input("请输入你刀子的长度"))
if knife<=10:
    print("可以上车")
else:
    print("记得在监狱写信`")
