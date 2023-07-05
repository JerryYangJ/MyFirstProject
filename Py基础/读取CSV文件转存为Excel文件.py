'''
@ 作者：JerryYang
@ 读取CSV文件，转存为Excel文件
'''

import pandas as pd

data = pd.read_csv('D:\桌面\QMS报表需求\原料表样例202204071444.csv', encoding='GBK')
print(data.head())
# writer = pd.ExcelWriter('D:\桌面\QMS报表需求\原料表样例202204071444.xlsx')