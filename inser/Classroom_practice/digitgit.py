def isdigit(content):
    flag=0
	#验证是否是数字
    for i in range(10):
        if str(i)==content:
            flag=1
            break
    return flag



def check_username(username):
	#检测username的长度
    if len(username)!=6:
        print("用户名必须6位")
        return    # 结束方法
	#检测首字母
    first_char=username[0]

	#调用isdigit()
    flag=isdigit(first_char)

    if flag==1:
        print("用户名首字母不能是数字，用户名错误！")
        return

    print("用户名验证成功！")


check_username("1旺财dog")

