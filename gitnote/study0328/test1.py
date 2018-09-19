import sys
a = 100
b = 100
print(a is b)


c=10000
d=10000
print(c is d)



print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))
print(sys.getrefcount(d))
print(globals())