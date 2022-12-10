import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt

pd.options.display.max_columns = 999
# 读取数据
data1 = pd.read_excel('./excel/IQC02005来料检验分类合格率分析2(管材)(8010).xls', header=1)
# print(data1)
# print(data1.columns)

# 删除空列
data1.drop(['Unnamed: 0'], axis=1, inplace=True)
# 删除空行
data1.dropna(inplace=True)
# print(data1)

# 转置
data1 = data1.transpose()
print(data1)
print(data1.columns)

# 写入文件
writer = pd.ExcelWriter('.\excel\IQC02005来料检验分类合格率分析2(管材)(8010).xls', engine='openpyxl')
data1.to_excel(writer, sheet_name='Sheet2')
writer.save()

print("over")
# # # 重新读取文件（重新读取后“合格率”才能自动转换为float型，否则为object类型，无法排序）
# data2 = pd.read_excel('.\excel\data2.xlsx', header=1)
# # # data2.drop(labels=[0, 1], inplace=True)
# data2.sort_values(by='合格率', inplace=True)
# print(data2)
# print(data2.dtypes)
#
# # 写入文件
# file = pd.ExcelWriter('.\excel\data3.xlsx')
# data2.to_excel(file, index=False)
# file.save()

# # # pyplot画图
# # plt.bar(data2['QMS小类'], data2['合格率'], color='orange')
# # plt.xticks(data2['QMS小类'], rotation='45')
# # plt.xlabel('QMS类别')
# # plt.ylabel('合格率')
# # plt.title('合格率', fontsize=18)
# # plt.tight_layout()
# # plt.show()
