from pymongo import MongoClient


def main():
    #套接字
    client = MongoClient("mongodb://127.0.0.1:27017")
    #获取数据库
    py3 = client["py3"]
    #获取文件
    sub = py3["sub"]
    #插入数据
    sub.insert({"title":"张旭","gender":"男"})
    #查询是否插入成功
    result = sub.find({"title":"张旭"})

    if result != None:
        print("插入成功")
    else:
        print("失败")
if __name__ == "__main__":
    main()