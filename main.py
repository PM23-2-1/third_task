import warnings

import universal
import db
import exel

warnings.filterwarnings("ignore")

def dict_1():
    list_1 = input('List 1: ').split()
    list_2 = input('List 2: ').split()
    if len(list_1) == len(list_2):
        dictionary = {k:v for k, v in zip(list_1, list_2) if list_1.count(k) == 1}
        print(dictionary)
        db.save_result('a:b', dictionary)
    else:
        print('Ошибка, количество элементов различается')
    return

def dict_2():
    dictionary = {i:i**3 for i in range(1, 11)}
    print(dictionary)
    db.save_result('dictionary', dictionary)
    return

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу в MySQL.
2. Создать первый словарь из двух списков и сохранить результаты в MySQL.
3. Создать второй словарь из двух списков и сохранить результаты в MySQL.
4. Все результаты вывести на экран из MySQL.
5. Все результаты сохранить в Excel.
6. Все результаты вывести на экран (в консоль) через Excel.
7. Завершить"""
    while run:
        run = universal.uni(commands, 
                      db.check_db, dict_1, dict_2,
                      db.print_db, db.save_db_to_xlxs, exel.print_exel)
    return

if __name__ == '__main__':
    main()