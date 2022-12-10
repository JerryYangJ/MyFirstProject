import pandas as pd

sheet20 = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet20')
sheet20_1 = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet20-1')

# 拼接两个df
students = pd.concat([sheet20, sheet20_1]).reset_index(drop=True)
print('使用concat拼接两个df：', '\n', students)

# 并排拼接两个df
students = pd.concat([sheet20, sheet20_1], axis=1)
print('使用concat拼接两个df：', '\n', students)

# # 将df写入文件
# file = pd.ExcelWriter('111.xlsx')
# students.to_excel(file)
# file.save()
# print('写入成功')