import pandas as pd

# pd.options.display.max_columns =999
left = pd.read_excel('.\excel\left.xlsx', sheet_name='Sheet1', index_col='物料编码')
right = pd.read_excel(r'.\excel\right.xlsx', sheet_name='Sheet1', index_col='物料编码')
# right = pd.read_excel('.\excel\\right.xlsx', sheet_name='Sheet1', index_col='物料编码')
print(right.head())

all_data = left.merge(right, how='left', on='物料编码')
print(all_data.head())

# writer = pd.ExcelWriter('.\excel\\all_data.xlsx', engine='openpyxl')
# all_data.to_excel(writer, sheet_name='Sheet1')
# writer.save()

