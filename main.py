while True:
    list1 = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"]

    birth = int(input("请输入您的年份"))

    position = birth % 12
    s = list1[position]

    print("您的生肖是:" + s)
