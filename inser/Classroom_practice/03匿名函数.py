stus=[
{'name':'zhangsan','age':18},
{'name':'lisi','age':20},
{'name':'wangwu','age':30}
]
print("yuanlaideliebiao=:",stus)
stus.sort(key=lambda x:x['name'])
print('排序后的列表=',stus)
stus.sort(key=lambda x:x['name'],reverse=True)
print('排序后的列表=',stus)
