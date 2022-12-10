import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet4')
print(books)
books.sort_values(by='Number', inplace=True, ascending=False)

# pandas画图
# books.plot.bar(x='Field', y='Number', color='orange', title='Student Number')
# books.plot(kind='bar', x='Field', y='Number', color='blue', title='Student Number')

# pyplot画图
plt.bar(books.Field, books.Number, color='orange')
plt.xticks(books.Field, rotation='45')
plt.xlabel('Student')
plt.ylabel('Number')
plt.title('Student Number', fontsize=18)
plt.tight_layout()
plt.show()
