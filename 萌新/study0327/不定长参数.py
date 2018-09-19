def huazhuang(func):
    print("---->即将要化妆...")

    # 化妆函数
    def makeup(age, *args, **kwargs):
        # 此时args就是一个元组
        func(age, *args, **kwargs)  # 记着传参如果是不定长参数就需要解包 *args   r
        print("---->洗脸")
        print("---->擦爽肤水，乳液")
        print("--->擦粉底或者BB爽")
        print("--->描眉,擦口红")
        for i in args:
            print("--->擦：%s" % i)
        print("--->照镜子：秒变18岁")

    return makeup


@huazhuang
def woman(age, *args, **kwargs):
    print("我已经有些老了...今年:%s" % age)
    for v in args:
        print("===>", v)
    # 打印字典中名字
    print(kwargs.get("name"))


list_ = ["眼影", "腮红", "假睫毛"]
dict_ = {"name": "王老太"}
woman(18, *list_, **dict_)  # （[]）

woman(20, "眼影", "腮红", "假睫毛", name="李老太")  # ("眼影", "腮红", "假睫毛")
