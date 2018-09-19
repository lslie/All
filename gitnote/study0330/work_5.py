import os
# 返回三个值0，大于0的值，-1
#如果返回0，当前是子进程
#如果返回大于0，当前是父进程
print("fork被调用前...")
pid = os.fork()
#注意fork函数只在Unix/Linux/Mac上运行，windows不可以
print("pid==",pid)
if pid == 0:
	print("我是子进程...pid=",pid)
elif pid >0:
	print("我是父进程...pid=", pid)
else:
	print("创建进程失败...", pid)
