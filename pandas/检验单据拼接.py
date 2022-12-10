# @Time :2022/10/19 13:30
# @Author : Jerry Y
# @File  : 检验单据拼接.py
# @Info  :

import pandas as pd

date = input("请输入月份日期（例：1018):")

# 读取管材检验单文件
data1 = pd.read_excel(f'./拼接/PQC04002过程检验单据查询_2022{date}(8010管材).xls', sheet_name='Sheet1')
data2 = pd.read_excel(f'./拼接/PQC04002过程检验单据查询_2022{date}(8012管材、市政).xls', sheet_name='Sheet1')
data_guanjian = pd.read_excel(f'./拼接/PQC04002过程检验单据查询_2022{date}(8010管件).xls', sheet_name='Sheet1')
# print(data1)

# 选择管材检验单中的"批号”列,并合并
se1 = data1['批号']
se2 = data2['批号']
se3 = data_guanjian['生产订单号']

se_pihao = pd.concat([se1, se2]).reset_index(drop=True)
# print(se_pihao)
# 删除重复项
se_pihao = se_pihao.drop_duplicates(keep='last')
se3 = se3.drop_duplicates(keep='last')
# 将”批号“中的”_"删除
se_pihao = se_pihao.str.replace('_', '')
# print(se_pihao)
# 将series转成DF1024
df = pd.DataFrame(se_pihao, columns=['批号'])
df['是否检测'] = se_pihao
df_guanjian = pd.DataFrame(se3, columns=['生产订单号'])
df_guanjian['是否检测'] = se3
# print(df_guanjian)

data3 = pd.read_excel('./拼接/每日生产订单统计表(管材).xlsx', sheet_name='管材8010')
data3 = data3.loc[:, ['生产工厂', '产品类别', '批号']]
data4 = pd.read_excel('./拼接/每日生产订单统计表(管材).xlsx', sheet_name='管材8012')
data4 = data4.loc[:, ['生产工厂', '产品类别', '批号']]
data5 = pd.read_excel('./拼接/每日生产订单统计表(市政).xlsx', sheet_name='管材')
data5 = data5.loc[:, ['生产工厂', '产品类别', '批号']]
data6 = pd.read_excel('./拼接/每日生产订单统计表(管件).xlsx', sheet_name='管件')
data6 = data6.loc[:, ['机台', '生产订单号']]
# print(data6)
# 合并8010、8012两个表
table_merge = pd.concat([data3, data4, data5]).reset_index(drop=True)

# 拼接表格
table = table_merge.merge(df, how='left', on='批号').fillna(0)
count_8010_1 = table.loc[table['生产工厂'].apply(lambda x: x == 8010)].loc[table['产品类别'].apply(lambda x: x == '管材')][
    '是否检测'].count()
# print("8010管材订单总数为：", count_8010_1)
count_8012_1 = table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '管材')][
    '是否检测'].count()
# print("8012管材订单总数为：", count_8012_1)
count_8012_2 = table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '市政')][
    '是否检测'].count()
# print("8012市政订单总数为：", count_8012_2)

table2 = data6.merge(df_guanjian, how='left', on='生产订单号').fillna(0)
# print(table2)

# 将文件写入文件
writer = pd.ExcelWriter('./拼接/结果.xlsx', engine='openpyxl')
table.to_excel(writer, sheet_name='Sheet1')
table2.to_excel(writer, sheet_name='Sheet2')
writer.save()
# t = table.groupby(['是否检测']).count()
t_8010_1 = table.loc[table['生产工厂'].apply(lambda x: x == 8010)].loc[table['产品类别'].apply(lambda x: x == '管材')].loc[
    table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
print("8010管材订单总数为：", count_8010_1, '\t', "未检测订单总数为：", t_8010_1)
t_8012_1 = table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '管材')].loc[
    table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
print("8012管材订单总数为：", count_8012_1, '\t', "未检测订单总数为：", t_8012_1)
t_8012_2 = table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '市政')].loc[
    table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
print("8012市政订单总数为：", count_8012_2, '\t', "未检测订单总数为：", t_8012_2)

# 管件
t_8010_guanjian = table2.loc[table2['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
count_8010_guanjian = table2['是否检测'].count()
print("8010管件订单总数为：", count_8010_guanjian, '\t', "未检测订单总数为：", t_8010_guanjian)
