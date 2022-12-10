'''
@ 作者：JerryYang
@ 将QMS不同工厂、QMS类别检验合格率分析报表数据转置、并按合格率排序后整合到同一个文件中
'''

import numpy as np
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt

pd.options.display.max_columns = 999
month = 3
# 读取数据
data1 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(包装材料)(8010).xls')
data2 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(包装材料)(8020).xls')
data3 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(包装材料)(8030).xls')
data4 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(包装材料)(8040).xls')
data55 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(包装材料)(8050).xls')
data5 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(玻璃胶)(8010).xls')
data6 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8010).xls')
data7 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8012).xls')
data8 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8020).xls')
data9 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8030).xls')
data10 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8040).xls')
data11 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管材)(8050).xls')
data12 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8010).xls')
data13 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8012).xls')
data14 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8020).xls')
data15 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8030).xls')
data16 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8040).xls')
data17 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(管件)(8050).xls')
data18 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8010).xls')
data19 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8012).xls')
data20 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8020).xls')
data21 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8030).xls')
data22 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8040).xls')
data23 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(塑料原材料)(8050).xls')
data24 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(卫浴)(8010).xls')
data25 = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(五金)(8010).xls')

# 将数据加入到一个列表
data_list = [data1,
             data2,
             data3,
             data4,
             data55,
             data5,
             data6,
             data7,
             data8,
             data9,
             data10,
             data11,
             data12,
             data13,
             data14,
             data15,
             data16,
             data17,
             data18,
             data19,
             data20,
             data21,
             data22,
             data23,
             data24,
             data25]

# 定义一个sheet_name_list，保存写入文件名
sheet_name_list = ('(包装材料)(8010)',
                   '(包装材料)(8020)',
                   '(包装材料)(8030)',
                   '(包装材料)(8040)',
                   '(包装材料)(8050)',
                   '(玻璃胶)(8010)',
                   '(管材)(8010)',
                   '(管材)(8012)',
                   '(管材)(8020)',
                   '(管材)(8030)',
                   '(管材)(8040)',
                   '(管材)(8050)',
                   '(管件)(8010)',
                   '(管件)(8012)',
                   '(管件)(8020)',
                   '(管件)(8030)',
                   '(管件)(8040)',
                   '(管件)(8050)',
                   '(塑料原材料)(8010)',
                   '(塑料原材料)(8012)',
                   '(塑料原材料)(8020)',
                   '(塑料原材料)(8030)',
                   '(塑料原材料)(8040)',
                   '(塑料原材料)(8050)',
                   '(卫浴)(8010)',
                   '(五金)(8010)')

# 定义一个writer
writer = pd.ExcelWriter(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\来料\IQC02005来料检验分类合格率分析{month}(合并).xlsx')

# 定义一个变量，作为sheet_name_list下标
n = 0

# 历遍data_list，逐个取出list中的df进行处理及写入文件
for data in data_list:
    # 清洗data
    data = data[0:5]    # 选取有用行
    data = data.dropna(axis=1, how='all')   # 删除空列
    data = data.set_index('Unnamed: 1', drop=True)  # 将第一列设置为行索引
    data = data.transpose()     # 转置
    data = data.set_index("QMS小类", drop=True)   # 将第一列设置为行索引

    # 转换data数据类型
    data["合格率"].astype("float")     # 将“合格率”列转换为float类型

    # 按合格率列排序
    data.sort_values(by="合格率", inplace=True)

    # 写入文件    ？？？输出时怎么把合格率转换成百分比？？？
    data.to_excel(writer, sheet_name=sheet_name_list[n], index=True)
    n = n + 1
writer.save()

print("over")


# # 测试代码
# data = data3
# print(data)
# data = data[0:5]
# data = data.dropna(axis=1, how='all')
# data = data.set_index('Unnamed: 1', drop=True)
# # print(data)
# data = data.transpose()
# # print(data)
# data = data.set_index("QMS小类", drop=True)
# print(data)










