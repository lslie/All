import random


# 函数校验登录:用户名,密码,角色,用户管理员

# 定义函数功能校验
def test(func):
    print("正在登录")

    def inner_test(**kwargs):
        if kwargs['name'] == 'admin' and kwargs['login'] == '123456':
            print("登录成功")
        else:
            num=random.randint(1000,9000)
            print(num)
            nums=input("请输入上方的验证码:")
            print(nums)
            if nums == num:
                print("登录成功用户状态")
    return inner_test


# 定义用户名密码
@test
def admin(**kwargs):
    print(kwargs)


names=input("请输入您是管理员还是用户")
admins = input("请输入您的账号:")
msg = input("请输入您的密码")
dicts = {'name': admins, 'login': msg}

b = admin(**dicts)
print(b)
