import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet18', dtype={'Month': str})
print(sales)

# 线性回归方程
slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')
plt.title(f'y={slope}*x+{intercept}')
plt.xticks(sales.index, sales.Month, rotation=45)
plt.tight_layout()
plt.show()
