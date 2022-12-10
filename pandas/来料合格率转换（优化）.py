import pandas as pd
import numpy as np

pd.options.display.max_columns = 999
# 读取数据
data1 = pd.read_excel('.\excel\来料\IQC02005来料检验分类合格率分析2(包装材料)(8010).xls')
data1=data1[0:5]
print(data1)
data1 = data1.dropna(axis=1, how='all')
print(data1)
# df_not_null.dropna(axis=0, how='all', inplace=True)
data1 = data1.transpose().set_index(0, drop=True)
print(data1)
