import pandas as pd

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet1', index_col='ID')
# books['Price'] = books['ListPrice'] * books['Discount']
# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
books['Price'] = books['ListPrice'].apply(lambda x: x + 2)
print(books)
