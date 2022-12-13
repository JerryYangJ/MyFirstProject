'''
@ 作者：JerryYang
@ 读取CSV文件，转存为Excel文件
'''

import pandas as pd

data = pd.read_csv('py基础/csv.csv', encoding='utf-8')
print(data.head())

def new_func(data):
    writer = pd.ExcelWriter('py基础/csv.xlsx')
    data.to_excel(writer, sheet_name="csv")
    writer.save()

new_func(data)