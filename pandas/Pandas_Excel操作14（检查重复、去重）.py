import pandas as pd

students = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet14')
dupe = students.duplicated(subset='Name')
print(dupe.any())
print(dupe)
dupe = dupe[dupe]       # dupe = dupe[dupe==Ture]
print(dupe)

# students.drop_duplicates(subset='Name', inplace=True, keep='last')
# print(students)
