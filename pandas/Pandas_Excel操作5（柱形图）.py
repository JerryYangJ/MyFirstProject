import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet5')
print(books)
books.sort_values(by='去年', inplace=True, ascending=False)
books.plot.bar(x='Field', y=['去年', '今年'], color=['orange', 'blue'])
plt.title('Student Number', fontsize=28, fontweight='bold')
plt.xlabel('Student', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
ax = plt.gca()  # 拿到图表对象的轴对象
ax.set_xticklabels(books.Field, rotation=45, ha='right')    # 设置旋转及旋转中心点
f = plt.gcf()  # 获取当前图表对象的图形区域对象
f.subplots_adjust(left=0.1, bottom=0.2)     # 设置图形边距
# plt.tight_layout()
plt.show()
