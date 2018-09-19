from pymongo import MongoClient

# client = MongoClient(
#     host="127.0.0.1",
#     port=27017
# )
client = MongoClient("mongodb://127.0.0.1:27017")
#得到数据库
py2 = client["py2"]
#得到集合
sub = py2["sub"]

# #得到数据库
# py2 = client.py2
# #得到集合
# sub = py2["sub"]


# result = sub.find({})

# for i in result:
#     print(i)

sub.insert({"name":"哈哈"})

result = sub.find({})

for i in result:
    print(i)