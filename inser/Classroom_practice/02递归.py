def digui(su):   #   参数是入口
    if su==1:      #这是出口
        return su
    else:
        return su+digui(su-1)    #su-1是不断接近出口
un=digui(10)     #因为是return所以要有变量进行接收
print(un)      #打印出来接收的值
