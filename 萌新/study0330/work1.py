#要求：请使用自定义元类的方式，把下面的代码能让
#print(p.COUNTRY)和p.TEST()正常调用
#创建方法
def bigger(name,parents,attr):
    new_attr={}
    for name,value in attr.items():
        new_attr[name.upper()] = value

    return type(name,parents,new_attr)

#创建类
class Person(object,metaclass=bigger):
    country='中国'

    def test(self):
        print("我是TEST函数，我被调用了")

p=Person()
print(p.COUNTRY)
p.TEST()