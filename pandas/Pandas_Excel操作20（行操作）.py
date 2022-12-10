import pandas as pd

sheet20 = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet20')
sheet20_1 = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet20-1')
print(sheet20, '\n', sheet20_1)

# 拼接两个表
students = sheet20.append(sheet20_1).reset_index(drop=True)

# 追加数据
stu = pd.Series({'ID': 41, 'Name': 'YY', 'Score': 99})
students = students.append(stu, ignore_index=True)

# 修改数据,方法1:修改单元格
students.at[39, 'Name'] = 'YJ'
students.at[39, 'Score'] = 99

# 修改数据,方法2：整行替换
stu1 = pd.Series({'ID': 39, 'Name': 'YX', 'Score': 100})
students.iloc[38] = stu1
print('修改数据：', '\n', students)

# 插入一行数据
stu2 = pd.Series({'ID': 101, 'Name': 'YK', 'Score': 101})
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu2, ignore_index=True).append(part2).reset_index(drop=True)
print('插入一行数据：', '\n', students)

# 删除数据行,方法1：drop方法
students.drop(index=[0, 1, 2], inplace=True)
print('删除数据行，方法1：drop：', '\n', students)

# 删除数据行，方法2：range方式
students.drop(index=range(3, 5), inplace=True)
print('删除数据行，方法2：range：', '\n', students)

# 删除数据行，方法3：切片方式
students.drop(index=students[5:10].index, inplace=True)
print('删除数据行，方法3：切片方法：', '\n', students)

# 有条件删除
delData = students.loc[students['Score'] > 80]
students.drop(index=delData.index,inplace=True)
students=students.reset_index(drop=True)    # 重设index
print('有条件删除（删除分数＞80）的行：', '\n', students)

