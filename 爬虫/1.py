"""
@author: JerryYang
@file: 1.py
@time: 2023/3/23 12:59
@desc:
"""
import os

os.system(f'ffmpeg -f concat -safe 0 -i D:/pythonProject/爬虫/movie/ts.txt -c copy 5.mp4')
# from random import randint
#
# for episode in range(1, 40):
#     print(episode)
# a = 20
# cs = 0
#
# for i in range(100):
#     b = randint(1, 100)
#     if b == a:
#         print(f"您{i}次抽中")
#     else:
#         print(f"对不起，您抽的第{i}次，未中奖")


# a = 20
# cs = 0
# for p in range(10000):
#     for i in range(100):
#         b = randint(1, 100)
#         if b == a:
#             cs = cs+1
#             # print(p, i, cs)
#             break
# print(cs)


