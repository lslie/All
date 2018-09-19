def number_index():
    sum=0
    while sum<=100:
        sum+=sum
        sum+=1
    return sum
str=number_index()
print(str)


def number_tur(num):
    i=0
    while i==num:
        i+=1
        print(i,num)
number_tur(100)


def number(num1):
    result=0
    i=1
    while i<=num1:
        result+=i
        i+=1
    return result
result=number(100)
print(result)
