import pandas as pd

pd.options.display.max_columns=998
videos = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet15')
print(videos)
table = videos.transpose()
print(table)