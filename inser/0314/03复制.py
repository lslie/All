#打开要复制的文件
old_file_name=input("请输入您要复制的文件名：")
old_file=open(old_file_name,'r')
#创建一个新文件用于保存要复制文件内容
new_file=open('atguigu.txt','w')



#读取要复制的文件，并且写到新文件中
read_content=old_file.read()
new_file.write(read_content)



#关闭两个文件夹
old_file.close()
new_file.close()
