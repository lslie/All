import random
names = ['袁绍','袁术','曹操','刘表','刘备','孙策','孙权','诸葛亮']
offices=[[],[],[]]   #建立办公室
for name in names:   #首先遍历各位老师
    index=random.randint(0,2)#随机办公室
    name_index=random.randint(0,len(name))
    offices[index].append(name)
i=1
for office in offices:
    name=names[name_index]
    if offices[index] not in name:
        offices.append(name)
        name!=name
    print('办公室%s:共%s人：'%(i,len(office)))
    i+=1
    for name in office:
        print("%s\t"%name,end='')
    print('')
    print('='*50)
