import os
import time
#父进程
pid = os.fork()
print("---------->马上启动")
time.sleep(1)
#启动一个进程 子进程
print("----------2")
time.sleep(1)
print("-------------3")


print('pid',pid)

if pid==0:
	print("子进程",pid)

elif pid>0:
	print("父进程",pid)
else:
	print("创建进程失败")