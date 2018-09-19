#创建心文本\
text=input('请输入您想输入的内容：')
f=open('程序员自我修养.txt','a')
f.write(text)
print('写入成功')
f.close()
import os
os.rename('程序员自我修养.txt','程序員自身修养.txt')
print('成功')
