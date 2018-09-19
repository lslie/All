def test():

    try:
        print("---->try")
        # print(num)
        # return 1
    except:
        print("----->except")
        # return 2
    else:
        print("---->else")
        return 0

    finally:
        print("----->finally")
        # return 3

value=test()

print(value)
