import pandas as pd


def age_18_to_30(a):
    return 18 <= a <= 30


def level_a(a):
    return 85 <= a <= 100


books = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet3', index_col='ID')
books = books.loc[books['Age'].apply(age_18_to_30)].loc[books['Score'].apply(level_a)]
# books=books.loc[books.Age.apply(age_18_to_30)].loc[books.Score.apply(level_a)]
# books = books.loc[books.Age.apply(lambda x: 18 <= x <= 30)].loc[books.Score.apply(lambda x: 85 <= x <= 100)]
print(books)
