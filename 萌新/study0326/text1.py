import copy
import study0326.twoRwo

a=['str1','str2',[1,2,3,["xy"]],'str3']
a1=copy.copy(a)
a1[2].append(5)
print(id(a[2]))
print(id(a1[2]))
