import os
print(os.getcwd())
os.mkdir("./test")
os.chdir("./test")
print(os.getcwd())
i=1
while i<=6:
    open ('人民的名义-%d.avi'%i,"w")
    i+=1
print('创建完毕！')
