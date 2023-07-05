# # 列表 用中括号
list1 = [123]
list2 = [234]
list3 = [345]
bool =list1 > list2
print(bool)
list4 = list1 +list2
print(list4)

bool1 = 123 in list1
print(bool1)

# 元组 用小括号或不用括号
# 一个元素的元组，后面加个逗号，否则不认为是元组
# 元组与列表的不同点是元组中的元素不可更改
# # 可以使用元组的计算重新定义一个元素，间接更改元组的元素
tuple1 = (1,2,3,4,5)
tuple2 = 1,2,3,4,5,6
tuple3 =(1,)
print(tuple1)
print(tuple2)
print(tuple3)
print(type(tuple3))

tuple4 = tuple1[:2] + (22,) + tuple1[2:]
print(tuple4)

