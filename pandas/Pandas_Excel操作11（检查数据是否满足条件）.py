import pandas as pd

i = 1


def scores_validation(row):
    global i
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'{i}、{row.ID}\t student {row.Name} has an invalid score {row.Score}.')
        i = i + 1

def scores_validation_1(row):
    global i
    if not 0<=row.Score<=100:
        print(f'{i}、{row.ID}\t student {row.Name} has an invalid score {row.Score}.')
        i = i + 1


students = pd.read_excel('PandasExcel.xlsx', sheet_name='Sheet11')
students.apply(scores_validation_1, axis=1)
# print(students)
