import pandas as pd

students = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet13', index_col='ID')
temp = students[['Test_1', 'Test_2', 'Test_3']]
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
students['Total'] = row_sum
students['Ave'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Ave']].mean()
col_mean['Name'] = 'Sum'
students = students.append(col_mean, ignore_index=True)     # ignore_index=True忽略索引，自动生成索引
print(students)
