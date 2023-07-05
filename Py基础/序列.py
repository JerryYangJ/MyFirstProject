"""
    @序列
    @主要有列表[]、元组()、集合{}、字典{}和字符串
    @列表、元组、字典、集合的去不区别
        数据结构               是否可变        是否重复          是否有序        定义符号
        列表(list)             可变           可重复            有序           []
        元组(tuple)            不可变         可重复            有序           ()
        字典(dictionary)       可变           可重复            无序           {key:value}
        集合(set)              可变           不可重复          无序           {}


             
"""
import random
from typing import List

"""
    @关键字
        in 关键字可以检查某个元素是否为序列的成员
    @内置函数
        len() 内置函数，计算序列的长度
        max() 内置函数，计算序列的最大值
        min() 内置函数，计算序列的最小值
        list()  内置函数，将序列转换为列表
        tuple() 内置函数，将序列转换为元组
        set()   内置函数，将列表、元组等可迭代对象转换为集合
        str()   内置函数，将序列装好为字符串
        sum()   内置函数，计算元素和
        sorted()    内置函数，对元素进行排序(原列表元素顺序不变）
        reversed()  内置函数，反向序列中的元素
        enumerate() 内置函数，将序列组合为一个索引序列，多用在for循环中
    @方法
        add()       向集合中添加元素
        append()    用于在列表末尾追加元素
        insert()    用于向列表的制定位置插入元素，效率低，不推荐
        extend()    将一个列表中的全部元素添加到另外一个列表中
        remove()    根据元素值删除一个不确定位置的列表元素
        pop()       根据索引值删除一个元素，并返回删除的元素值；使用del删除元素不能返回删除的元素值
        count()     获取指定元素在列表中出现的次数
        index()     获取指定元素在列表中首次出现的位置索引
        sort()      listname.sort(key=None,reverse=False);key表示指定的从每个元素纵提取一个用于比较的键（如：设置”key=str.lower",
                    表示在排序时不区分字母大小写）；reverse的值为True，则表示降序排列，反之为升序排列，默认升序
                    @sort()方法和内置函数sorted()函数的作用基本相同；不同点是在使用sort()方法时，会改变原列表元素的排列顺序，而使用
                    sorted()函数时，会建立一个原列表的副本，该副本为排序后的列表
                    
"""

"""
    @列表推导式
        1.生成指定范围的数值列表
            list = [Expression for var in range]    
                Exception   表达式，用于计算新列表的元素
                var         循环变量
                range       采用range()函数生成的range对象
        2.根据列表生成指定需求的列表
            newlist = [Expression for var in list]
                Exception   表达式，用于计算新列表的元素
                var         循环变量
                list        用于生成新列表的原列表
        3.从列表中选择符合条件的元素组成新的列表
            newlist = [Expression for var in list if condition]
                Exception   表达式，用于计算新列表的元素
                var         循环变量
                list        用于生成新列表的原列表
                condition   表达式，用于指定筛选条件
"""

"""
    @列表和元组的区别
        1.列表属于可变序列，它的元素可以随时修改或者删除；元组属于不可变序列，其中的元素不可以修改，除非整体替换
        2.列表可以是使用append()、extend()、insert()、remove()和pop()方法实现添加和修改列表，元组不行
        3.列表可以使用切片访问和修改列表中的元素。元组也支持切片，但是它只支持通过切片访问元素，不支持修改
        4.元组比列表的访问和处理速度快，如果只是需要对其中的元素进行访问，不进行修改时，建议使用元组
        5.类别不能作为字典的键，而元组可以
"""

"""
    @字典{}
        特征：
            1.通过键而不是通过索引来读取
            2.字典时任意对象的无需集合
            3.字典时可变的，并且可以任意嵌套
            4.字典中的键必须唯一
            5.字典中的键必须不可变（所以键不可使用列表）
        创建：
            dictionary = {} 或  dictionary = dict()   
        
            使用dict()方法创建字典
                1.dictionary = dict(zip(list1,list2)
                    zip()函数：用于将多个列表或元组对应位置的元素组合为元组，闭关返回包含这些内容的zip对象。如果想回去元组，可以将zip对应使用
                        tuple()函数转换这些元组；如果想获取列表，使用list()方法转换
                    list1：一个列表，用于指定要生成字典的键
                    list2：一个列表，用于指定要生成字典的值。如果list1和list2长度不同，则与最短的列表长度相同
        
"""




nba = [1, 3, 5, 4, 2]
nba1 = ["1", "3", "5", "4", "2"]
print("1" in nba)
print("序列", nba, "的长度为：", len(nba))
print("序列", nba, "中最大值为：", max(nba))
print("序列", nba, "中最小值为：", min(nba))
print("序列", nba, "转换为列表：", list(nba))
print("序列", nba, "转换为字符串：", str(nba))
print("序列", nba, "元素和为：", sum(nba))
print("序列", nba, "排序为：", sorted(nba))
print("序列", nba, "使用函数排序后原列表元素顺序不变", nba)
print("序列", nba, "反向序列中的元素：", reversed(nba1))     #????


"""
    @列表
"""
list1 = list(range(10))     #使用range()函数创建列表
print(list1)


for item in list1:   # 使用for循环历遍列表
    print(item)

for index, item in enumerate(list1):        # enumerate()函数可输出索引值
    print(index + 1, "\t\t\t", item)        # \t 打印制表符；   \n 换行

list1.append(10)    # 用于在列表末尾追加元素
print(list1)

nba.extend(nba1)    # 将一个列表中的全部元素添加到另外一个列表中
print(nba)

#   修改列表元素：通过索引值

nba[2] = "我是被修改的"
print(nba)

#   通过索引值删除元素
print("删除前列表为：", nba)
del nba[2]
print("删除索引值为2后的列表为：", nba)

#   通过元素值删除元素,如果指定元素值不存在，会报错，最好先做判断是不存在。
print("删除前列表为：", nba)
nba.remove("1")
print("删除列表元素1后前列表为：", nba)
nba.remove(1)
print("再删除列表元素为""1""后的列表为：", nba)

#   列表元素的统计和计算
listname = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print("列表为：", listname)
num = listname.count(2)                 # count()方法，计算元素在列表中出现的次数
print("数字2在列表中出现了", num, "次")

#   获取指定元素在列表中首次出现的位置索引
num1 = listname.index(4)
print("数字4在列表中首次出现的位置（索引)为：", num1, "，它在列表的第", num1 + 1, "位")

#   数值列表排序
grade = [9, 8, 10, 6, 4, 1, 2, 5, 3, 7]
print("原列表：", grade)
grade.sort()
print("升序排列：", grade)
grade.sort(reverse=True)
print("降序排列：", grade)

#   字符串排序
char = ['cat', 'Tom', 'Angela', 'pet']
print("原列表：", char)
char.sort()
print("默认区分大小写排序：", char)
char.sort(key=str.lower)
print("不区分大小写排序：", char)


#   生成一个包括10个随机数的列表，要求数的范围在10~100之间
randomnumber =[random.randint(10,100) for i in range(10)]
print("生成的随机数为：", randomnumber)
a = randomnumber.pop()
print(a)
print("删除最后一个元素后为：", randomnumber)
randomnumber = tuple(randomnumber)      #转换为元组
print(randomnumber)


#   通过映射创建字典
    # 定义两个列表，使用dict()函数和zip()函数将列表转换为对应的字典
list1 = ["张三", "李四", "王五"]
list2 = ["25", "24", "28"]
dictionary1 = dict(zip(list1, list2))
print(dictionary1)

#   通过给定的“键-值”创建字典
