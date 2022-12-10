import pandas as pd

students = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet12', index_col='ID')
df = students['Full Name'].str.split(expand=True)
students['Fist Name'] = df[0]
students['Last Name'] = df[1]
print(students)
