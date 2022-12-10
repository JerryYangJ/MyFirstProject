import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet6')
books['Total'] = books['Oct'] + books['Nov'] + books['Dec']        # 增加一个总数列，用于排序
books.sort_values(by='Total', inplace=True, ascending=False)       # 用总数列排序
print(books)
books.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='UserS')   # bar与barh
plt.tight_layout()
plt.show()
