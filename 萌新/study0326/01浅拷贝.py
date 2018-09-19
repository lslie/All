import copy
will=['will',28,['copy','c#','js']]
wilber=copy.copy(will)
print('will的id:',id(will))
print("wilber的id",id(wilber))
print("will",will)
print("wilber",wilber)
print("wil all id",[id(item) for item in will])

print("wilber的所有id",[id(item) for item in wilber])

print('**'*50)
will[0]='wilber'
will[2].append('css')
print("will id",id(will))
print("will:",will)
print("will all id",[id(item) for item in will])
print("wilber id",id(wilber))
print("wilber",wilber)
print("wilber all id",[id(item) for item in wilber])