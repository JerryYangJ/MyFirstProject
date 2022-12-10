import pandas as pd

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet2', index_col='ID')
books.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[True, True])
print(books)
