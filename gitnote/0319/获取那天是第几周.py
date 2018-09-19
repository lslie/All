#coding=utf-8
import time
from datetime import datetime

#52 今天是52周
print(time.strftime("%W"))
#2，因为今天是周三，周一是0
today = datetime.now().weekday()
print(today)
#52 20171225是52周
week = datetime.strptime("2018319","%Y%m%d").strftime("%W")
print(week)