import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet8', index_col='Week')
print(weeks)
print(weeks.columns)

weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components'])    # plot折线图
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])   # plot.area叠加区域图
weeks.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Components'], stacked=True)  # 叠加区域图
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)
plt.show()
