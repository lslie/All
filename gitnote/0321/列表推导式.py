#coding=utf-8
# def list(list):
#     return [ x.upper() for x in (isinstance(list,str))
# list1=["hello"]
# list=list(list1)

def number():
    return ['%sx%s'%(x,x+1) for x in range(1,100,2)]
a=number()
print (a)


def list():
    return [

        a*100+b*10+c
        for a in range(1,10)
        for b in range(1,10)
        for c in range(0,10)
        if a==c
    ]


c=list()
print(c)
