#1获取图片的名字
#2定义一个picture类
#3属性id,name
#3创建四个图片对象
#4创建一个继承mypicture继承picture添加私有的__dize
str=["http://www.baidu.com/img/logo.png","http://www.baidu.com/img/pic.png","http://www.baidu.com/img/flower.png","http://www.baidu.com/img/tree.png"]

str1=[x[x.rfind('/')+1:x.rfind('.')] for x in str]
print(str1)


class Picture(object):
	def __init__(self,id,name):
		id=id
		name=name
	def pictures(self,str1):
		for item in str1:
			print('http://www.baidu.com/img/'+item+'.png')
	def __str__(self):
		msg='id:'+self.id+'name'+self.name
		return msg

class Mypicture(Picture):
	def __init__(self):
		__dize=40

picture=[Picture(id,name) for id,name in Picture.pictures()]
print(picture)
mypicture=Mypicture()

