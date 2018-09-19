a=[1,2,3,4]
b=a;
print(id(a))
print(id(b))
print('%s'%a)
a.append("1")
print(id(a))
print(id(b))
print('%s'%a)
print('%s'%b)
str='abc'
str1='abc'
print(id(str))
print(id(str1))

