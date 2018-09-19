def text1():
    print("="*50)
def text2(i):
    x=0
    while x<=i:
        text1()
        x+=1
text1();
nu=int(input("请输入打印数量："))
text2(nu)
