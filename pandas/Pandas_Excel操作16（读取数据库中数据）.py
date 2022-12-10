import pandas as pd

students1 = pd.read_csv('excel\Students.csv', index_col='ID')
students2 = pd.read_csv('excel\Students.txt', sep='|', index_col='ID')
print(students2)

