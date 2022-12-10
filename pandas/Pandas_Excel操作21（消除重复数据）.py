import pandas as pd

students= pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet21')
print(students)

# 删除重复数据
students.drop_duplicates(subset=['Name','Test_1'], inplace=True, keep='last')
print(students)