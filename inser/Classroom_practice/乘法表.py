#编程实现9*9乘法表-函数版
#使用循环嵌套
def ride_sum(n):
    for i in range(n):
       i=1
       while i<=9:
          j=1
          while j<=i:
              print('%d*%d=%d\t' %(i,j,i*j),end="")
              j+=1
          i+=1
          print('')
num=int(input("请输入您要打印的次数"))
ride_sum(num)
