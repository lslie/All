while True:
    enter_info=input("请输入内容：")
    if enter_info=='exit':
        print('退出')
        break;
    elif enter_info.isdigit():
        print('您输入的是数字')
    elif enter_info.isalpha():
        print('您输入的是字母')
    elif enter_info.lower().startswith("http://")and \
        enter_info.lower().endswith('.com'):
        print("您输入的是网址")
        print('您输入的是字母跟数字')
    elif enter_info.lower().endswith('.py'):
        print('您输入的是一个python文件')
