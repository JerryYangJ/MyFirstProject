print("今有物不知数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(100):
    if number%3 == 2 and number%5 == 3 and number%7 == 2:
        print(number)

print("今有物不知数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number1 = 0
while number1 <1000:
    number1 += 1
    if number1 % 3 == 2 and number1 % 5 == 3 and number1 % 7 == 2:
        # print(number1,end="/")      # ,end="分隔符"，标识输出内容在同一行显示，并使用”分隔符“隔开
        print(number1, end=" ")
        break

str1 = "不要说我不行！"
print("\n")     # \n，换行
print(str1)     # 横向显示
for i in str1:
    # print(i,end="")       # 横向显示
    print(i)            # 纵向显示