import random
def suiji():
    a = ['王璠', '李明', '郑昕', '张旭', '樊杰', '孙凤春', '邵栋', '王维', '王迪',
         '陈壮', '张晓飞', '罗鹏程', '冯磊', '高瑞伟', '闫茂雷', '尚玉磊']
    print("请开始你的表演！")
    kaishi=input("输入1开始输入0退出：")
    if kaishi=="1":
        a.reverse()
        print(random.choice(a))
        suiji()
    elif kaishi=="0":
        return
    else:
        print("输入有误!")
        suiji()
suiji()
