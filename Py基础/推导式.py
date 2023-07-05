"""
@author: JerryYang
@file: 推导式.py
@time: 2023/6/21 16:19
@desc:
"""

# @列表推导式
# [表达式 for 变量 in 列表] 或 [表达式 for 变量 in 列表 if 条件]
names = ['Bob', 'Tom', 'jerry', 'wendy', 'Smith', 'alice']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# @字典推导式
# { key_expr: value_expr for value in collection }或 { key_expr: value_expr for value in collection }
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)

newdict2 = {key: value for key, value in enumerate(listdemo)}
print(newdict2)

list = [x + 1 for x in range(10)]
print(list)
list2 = [x if x % 2 == 0 else 'x' for x in list]
print(list2)

a = []
for x in list:
    # print(x)
    if int(x) % 2 == 0:
        a.append(x)
print(a)
