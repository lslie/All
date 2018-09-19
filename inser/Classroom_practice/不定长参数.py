#不定长参数：
'''
下载download(url,*args)
'''
def download(url,*args):
    print('='*50)
    if len(args)<0:
        print("路径错误")
    else:
        for i in range(len(args)):
            print("下载%d张图片:%s"%((i+1),args[i]))

url=input("请输入您要下载的地址：")
download(url,'a1,jpg')
