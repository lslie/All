import os
import time
#pid
pid=os.fork()
print("进程开启之后")
if pid==0:
    print("子进程我的当前id =%d,我父进程的id=%d"%(os.getpid(),os.getppid()))
elif pid>0:
    print("常见父进程我的当前id =%d,我父进程的id=%d"%(os.getpid(),os.getppid()))
print("代码结束")