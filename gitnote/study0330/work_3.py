#玩游戏
def play():
	for i in range(3):
		print("玩游戏",i)
		yield None

#带孩子
def look_child():
	for i in range(3):
		print("带孩子",i)
		yield None

if __name__=="__main__":
	p=play()
	l=look_child()

	try:
		while True:
			p.__next__()
			l.__next__()
	except:
		print("活干完了")
	finally:
		print("休息")