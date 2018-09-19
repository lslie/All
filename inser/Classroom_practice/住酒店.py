card_id=input("带没带身份证？")#1代表有身份证0代表没有
if card_id=="带了":
    print("可以今晚开房")
    money=int(input("带了多少钱？"))
    if money>=300:
        print("今晚戴套！")
    else:
        print("不行了钱不够！不带了！")
else:
    print("没钱还谈恋爱？食屎啊！")
