from pymongo import MongoClient


def main():
    #套接字
    client = MongoClient("mongodb://127.0.0.1:27017")

    #套接字选择mongodb数据库
    py3 = client["py3"]
    #数据库选择文档
    sub = py3["sub"]
    #查找find
    result = sub.find({})
    for i in result:
        print(i)

if __name__ == "__main__":
    main()