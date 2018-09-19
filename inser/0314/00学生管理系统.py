#1.添加用户----》磁盘中----》users.txt用来保存添加的用户---》一个用户一行---》str=name age sex addrgress 
                                                                          #--->{'name''age''sex''addrgess'}
#2.查询用户-----》读取users.txt中的数据-----》没读取一行就是一个用户信息
#3.修改学生信息  选择修改那一项，姓名年龄性别地址
#4.删除学生信息：自由发挥
#添加学生信息
def add_student():
    #结合文件
    f=open('user.txt','a')
    #使用f进行写操作
    f.write(input('输入姓名'))
    f.write(''+input('输入年龄'))
    f.write(''+input('输入性别'))
    f.write(''+input('输入地址'))
    f.write('\n')
    f.close()
    print('添加成功')
#查询学生信息:
def search_student():
    print('所有学生信息')
#查询文件
    f=open('user.txt','r')
    #按照行读取内容
    while True:
        line=f.readline()
        if len(line)==0:
            break
    f.close()


#学生管理系统
def system_manager():
    while True:
        print('='*50)
        print('1.添加学生信息')
        print('2.查询学生信息')
        print('='*50)
        choice=input("请输入您的选择：")
        #判断你的选择
        if int(choice)==1:
            #添加学生信息
            add_student()

        elif int(choice)==2:
            #查询学生信息
            search_student()


        elif int(choice)==3:
            print('退出')
            break


#调用学生管理系统
system_manager()
