"""
定义一个函数完成
前2个数完成加法运算
然后对第3个数，进行减法
然后调用这个函数使用def定义函数
要注意有3个参数
调用的时候，这个函数定义时有几个参数
那么就需要传递几个参数。
"""
def plus_sub(one,two,three):
    one=one+two
    three=one-three
    return three

one=int(input("请输入第一个数："))
two=int(input("请输入第二个数："))
three=int(input("请输入第三个数："))
str=plus_sub(one,two,three)
print("前两个数相加减去第三个数结果为:%d"%str)
