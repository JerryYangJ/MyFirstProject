# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5

fish = 6
a = 0
while True:
    total = fish
    enough = True
    for i in range(5):
        if (total-1) % 5 == 0:
            total = (total-1)/5*4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    else:
        fish += 5
    a += 1
print(f"while循环次数{a}")
