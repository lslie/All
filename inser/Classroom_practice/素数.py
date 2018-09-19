def is_prime(n):
    if n%400==0:
        return True
    elif n%4==0 and n%100!=0:
         return True
n=int(input("请输入您要查询的年份"))
um=is_prime(n)
print(um)
