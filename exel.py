import pandas as pd
def print_exel():
    name = input('Путь до файла и название: ')
    new_df = pd.read_excel(name)
    print(new_df)
    return