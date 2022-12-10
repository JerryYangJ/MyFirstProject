import numpy as np
import pandas as pd


pd.options.display.max_columns = 999
month = 3
# 读取数据
data1 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8010).xls', skiprows=[6, 7, 8], header=1, index_col=0,
                      usecols=[1, 2, 3, 4, 5])
data2 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8020).xls', skiprows=[6, 7, 8], header=1, index_col=0,
                      usecols=[1, 2, 3, 4, 5])
data3 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8030).xls', skiprows=[6, 7, 8], header=1, index_col=0,
                      usecols=[1, 2, 3, 4, 5])
data4 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8040).xls', skiprows=[6, 7, 8], header=1, index_col=0,
                      usecols=[1, 2, 3, 4, 5])
data5 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8050).xls', skiprows=[6, 7, 8], header=1, index_col=0,
                      usecols=[1, 2, 3, 4, 5])

# 将数据加入到一个列表
data_list = [data1, data2, data3, data4, data5]

# 定义一个sheet_name_list，保存写入文件名
sheet_name_list = ('（包装材料）8010', '（包装材料）8020', '（包装材料）8030', '（包装材料）8040', '（包装材料）8050')

# 定义一个writer
writer = pd.ExcelWriter('合并.xlsx')

# 定义一个变量，作为sheet_name_list下标
n = 0

# 历遍data_list，逐个取出list中的df进行处理及写入文件
for i in data_list:
    i.reset_index(inplace=True)
    i = i.transpose()
    i.dropna(axis=0, how='all', inplace=True)
    print(i)
    i.to_excel(writer, sheet_name=sheet_name_list[n], index=True)
    n = n+1
writer.save()


print("over")
