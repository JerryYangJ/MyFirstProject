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

# 定义一个sheet_name_list，保存读取的文件名后缀及写入文件的sheet名
sheet_name_list = ('(管材)(8010)',
                   '(管材)(8012)',
                   '(管材)(8020)',
                   '(管材)(8030)',
                   '(管材)(8040)',
                   '(管材)(8050)',
                   '(管件)(8010)',
                   '(管件)(8020)',
                   '(管件)(8030)',
                   '(管件)(8040)',
                   '(管件)(8050)',
                   '(卫浴)(8010)',
                   '(五金)(8010)',
                   '(玻璃胶)(8010)')

# 定义一个writer
writer = pd.ExcelWriter(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\制程\PQC04008过程检验合格率统计{month}(合并).xlsx')

# 定义一个变量，作为sheet_name_list下标
n = 0

# 逐个读取文件进行处理及写入文件
for name in sheet_name_list:
    data = pd.read_excel(f'D:\月报\QMS系统数据（2022年）\QMS检验数据（{month}月）\制程\PQC04008过程检验合格率统计{month}{name}.xls')
    # 清洗data
    data = data[3:9]  # 选取有用行
    data = data.dropna(axis=1, how='all')  # 删除空列
    data = data.set_index('Unnamed: 1', drop=True)  # 将第一列设置为行索引
    data = data.transpose()  # 转置
    data = data.set_index("项目", drop=True)  # 将第一列设置为行索引

    # 转换data数据类型
    data["合格率"].astype("float")  # 将“合格率”列转换为float类型

    # 按合格率列排序
    data.sort_values(by="合格率", inplace=True)

    # 写入文件    ？？？输出时怎么把合格率转换成百分比？？？
    data.to_excel(writer, sheet_name=sheet_name_list[n], index=True)
    n = n + 1
writer.save()

print("over")
