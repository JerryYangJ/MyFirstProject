# @Time :2022/10/3 7:08
# @Author : Jerry Y
# @File  : 多线程测试.py
# @Info  :
import time
from concurrent.futures import ThreadPoolExecutor

i = 1
n = 1


def xiancheng(i, n):
    time.sleep(1)
    print(f'线程{i}：n={n}')
    i += 1


with ThreadPoolExecutor(20) as t:
    for i in range(1, 1000):
        t.submit(xiancheng, i, n)
        n += 1

