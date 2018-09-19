age=int(input("请输入您的年龄："))
if age>=0 and age<3:
    print("有婴儿时期")
elif age>=3 and age<12:
    print("儿童时期")
elif age>=12 and age<=17:
    print("青春期")
elif age>=18 and age<=24:
    print("青年期")
elif age>=25 and age<=44:
    print("壮年期")
elif age>=45 and age<=60:
    print("中年时期")
else:
    print("祝您长命百岁")
