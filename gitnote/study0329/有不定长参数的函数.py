from time import ctime,sleep
def func(func_name):
   print("func...")
   def func_in(*args,**kwargs):
         print("%s在%s被调用..."%(func_name.__name__,ctime()))
         func_name(*args,**kwargs)
   return func_name
@func
def test(a,b,c):
   print("test...")
   print(a+b+c)

@func
def get_info():
   return"--你这个死鬼--"

test(10,20,30)
print(get_info())
