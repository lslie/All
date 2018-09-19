import functools
#functools模块的wraps函数的作用，请用案例说明
#创建装饰器
def test(func):
    "这是装饰器"
    @functools.wraps(func)
    def inner_test():
        "嵌套函数的文档说明"
        print("执行了嵌套函数")
        return func()
    return inner_test

@test
#创建方法
def person():
    "doc文档说明这是被装饰的函数"
    print('这是方法')
person()
print(person.__doc__)