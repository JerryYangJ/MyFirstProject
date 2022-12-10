import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777  # 设置显示列宽
homes = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet9')
print(homes.head())

# homes.plot.scatter(x='sqft_living', y= 'price')     # 散点图
# homes.plot.scatter(y='sqft_living', x= 'price')
# homes['sqft_living'].plot.hist()  # 直方图
# plt.show()
# homes.sqft_living.plot.hist(bins=100)  # 直方图
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
# homes.price.plot.hist(bins=100)  # 直方图
# # plt.xticks(range(0, max(homes.price), 100000), fontsize=8, rotation=90)
homes.sqft_living.plot.kde()  # 密度图，密度图可以了解到数据分布的密度情况
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
plt.show()
print(homes.corr())  # 分析数据表中每两列数据之间的相关性
