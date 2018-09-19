#1、添加用户
#2、查询用户
#3、修改信息
#4、删除学生信息

#添加学生信息
def add_student():
    stream=open("user.txt","a")
    stream.write(input("请输入姓名："))
    stream.write(" "+input("输入年龄："))
    stream.write(" "+input("输入性别："))
    stream.write(" "+input("输入地址："))
    stream.writr("\n")

    stream.close()


    print("添加新用户成功！")


#查询学生信息
def search_student():
    print("所有的学生信息如下：")
    stream=open("user.txt",'r')
    while True:
        line=stream.readlines()
        print(line)
        if len(line)==0:
            break

    stream.close()


#修改学生信息

def alter_student():
    name=print(input("请输入您要修改的学生的姓名"))
    stream=open('user.txt','r')
    lines=stream.readlines()
    stream.close()
    for str in lines:
        if str.find(name)!=-1:
            lines.remove(str)
	    age=input("请输入要修改的年龄")
	    sex=input("请输入要修改的性别")
	    address=input("请输入要修改的地址")
	    i_new=name+" "+age+" "+sex+" "+address
	    lines.append(i_new)
	    break
	i_s='\n'.join(lines)
	stream=open("user.txt","w")
	stream.write(i_new)
	stream.close()
#删除学生信息
def delete_student():
    name=input("请输入一个姓名")
    stream = open("user.txt", "r")
    lines = stream.readlines()
    stream.close()
    for str in lines:
        if str.find(name) != -1:
	    lines.remove(str)
            break
    str="\n".join(lines)
    stream = open("user.txt", "w")
    stream.write(str)
    stream.close()
#定义系统
def system_student():
    while True:
        print('='*50)
	print('1、添加学生信息')
	print('2、查询学生信息')
	print('3、修改学生信息')
	print('4、删除学生信息')
	print('5、退出系统')
	print('='*50)
	choice=int(input("请输入您的选项"))
        #判断
	if choice==1:
	    add_student()
	elif choice==2:
	    search_student()
	elif choice==3:
	    alter_student()
	elif choice==4:
	    delete_student()
	elif choice==5:
	    print("退出系统！")
	    break

