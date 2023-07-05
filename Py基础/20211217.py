# print(5+3)
# print("well water"+"river")
# print("well water"+" river")
# print("well water"*8)
# print("well water\n"*8)
# print("well water"+8)    #报q错


JS = input("猜猜我心里想的是什么数字：")
guess = int(JS)
while guess!=8:
    print("你猜错了，请重新输入吧")
    JS=input("猜猜我心里想的是什么数字：")
    guess=int(JS)
    if guess==8:
        print("恭喜你，猜对了")
    else:
        if guess==7:
            print("猜错了，不过很接近了，继续加油")
        else:
            if guess == 9:
                print("猜错了，不过很接近了，继续加油")
            else:
                print("猜错了")
print("游戏结束")

