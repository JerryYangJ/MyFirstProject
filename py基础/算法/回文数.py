# @Time :2022/12/2 8:13
# @Author : Jerry Y
# @File  : 回文数.py
# @Info  :

import random

# num = input("请输入数据：")
n = input("输入最大数字：")

for i in range(0, int(n)):
    num_str_r = ''.join(reversed(str(i)))
    if str(i) == num_str_r:
        print(int(i))



# def rev_str_thru_join_revd(STR):
#     return "".join(reversed(STR))
#
# INPUT_STRING = "Linuxize"
# a =rev_str_thru_join_revd(INPUT_STRING)
#
# if __name__ == '__main__':
#
#     print(a)
#     # print("RESERVED STRING THROUGH JOIN & REVERSED", rev_str_thru_join_revd(INPUT_STRING))

