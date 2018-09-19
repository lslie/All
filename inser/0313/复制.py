#打开你要复制的文件
old_name=input("请输入您要复制的文件名：")
f=open(old_name,'r')
#第一：要复制test.py复制后名字叫:[复制]test.py的做法
#new_name='[复制]'+old_name
#第二：要求test.py-----》test[复制].py
#1。得到.的位置
position= old_name.rfind('.')
#得到.的前面部分
pre=old_name[:position]
#3得到.后面的部分包括.
sux=old_name[position:]
#4new_name=前面部分+[复制部分]+后面部分
new_name=pre+"[复制]"+sux
new_file=open(new_name,'w')


#读取要复制的文件，并且写到心文件中
read_content=f.read()
new_file.write(read_content)
f.close()
new_file.close()
