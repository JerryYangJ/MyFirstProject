import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet7', index_col='Field')
print(books)
# books.sort_values(by='2022', inplace=True, ascending=False)     # 排序，也可以使用Series进行排序
books['2022'].sort_values(ascending=False).plot.pie(fontsize=8, startangle=270)  # pie 饼图：只需要一列数据，一个Series  # startangle开始角度
books['2022'].plot.pie(fontsize=8, counterclock=False, startangle=90)  # counterclock正逆时针
plt.title('Student Information', fontsize=14, fontweight='bold')
plt.ylabel('2022', fontsize=25, fontweight='bold')
plt.show()

