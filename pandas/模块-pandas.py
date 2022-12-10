import pandas as pd

# files = pd.read_excel("books.xlsx", sheet_name="Sheet1")
# L1 = [100, 200, 300]
# L2 = ['x', 'y', 'z']
# s1 = pd.Series(L1, index=L2)
s1 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s1)

s2 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s3 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s4 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
df = pd.DataFrame({s2.name: s2, s3.name: s3, s4.name: s4})  # 将Series以字典方式加入DataFrame,以列的方式
df1 = pd.DataFrame([s2, s3, s4])  # 将Series以list列表方式加入DataFrame,以行的方式
print(df)
print(df1)
