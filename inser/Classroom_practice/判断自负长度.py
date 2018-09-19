import sys
try:
    size=int(input("输入您想判断的字符的字节长度："))
except:
    size=input("请输入您想判断的字符的长度：")
su=sys.getsizeof(size)
print("您输入的字符的字节长度为%s"%su)
