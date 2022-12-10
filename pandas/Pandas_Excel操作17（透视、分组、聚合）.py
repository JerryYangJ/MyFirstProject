import pandas as pd
import numpy as np

pd.options.display.max_columns = 998
orders = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet17')
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
# print(orders.head())

# # 第一种方法实现透视
# pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)  # aggfunc聚合函数
# print(pt1)

# 第二种方法，使用groupby进行分组
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)
