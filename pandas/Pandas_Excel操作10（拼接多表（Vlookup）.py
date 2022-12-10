import pandas as pd


students = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet10', index_col='ID')
scores = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet10-1', index_col='ID')
table = students.merge(scores, how='left', on='ID').fillna(0)   # merge 联合多表；how 保留未匹配的数据的方式；fillna填充未匹配的数据；两个表的列名一样时可以使用on
# table = students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)       # 第二种联合方式
# table = students.merge(scores, how='left', left_on=students.ID, right_on=scores.ID).fillna(0)       # 第三种方式，前提是ID列不可设置为index
# table = students.join(scores, how='left', on='ID').fillna(0)    # join没有left_on和right_on,默认使用index进行联合
table.Score = table.Score.astype(int)  # 将数据转换为整数
print(table)
