import pandas as pd

books = pd.read_excel('pandas/质量控制部.xlsx', usecols='A:E', index_col='序号')
books.sort_values(by='工号', inplace=True, ascending=False)   #  sort_values 排序  by排序的列(可传列表） inplace=True在原S内排序，不新生成S；ancending排序方式（可用列表，与列对应）
print(books)
