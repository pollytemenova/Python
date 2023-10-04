# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.

from csv import DictWriter, DictReader
from os.path import exists


def create_file():
    with open('phone.csv', 'w', encoding='UTF-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()


def get_info():
    mas_info = ['Иванов', 'Иван', 123]
    return mas_info


def write_file(lst):
    with open('phone.csv', 'r', encoding='UTF-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    with open('phone.csv', 'w', encoding='UTF-8', newline='') as data:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            f_writer.writerow(el)


def read_file(file_name):
    with open(file_name, encoding='UTF-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res


def change_file(lst):
    with open('phone.csv', 'r', encoding='UTF-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    with open('phone.csv', 'w', encoding='UTF-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            if el['Фамилия'] == lst[0]:
                el['Имя'] = lst[1]
                el['Номер'] = lst[2]
            if el['Имя'] == lst[1]:
                el['Фамилия'] = lst[0]
                el['Номер'] = lst[2]
            f_writer.writerow(el)


def delete_data(lst):
    with open('phone.csv', 'r', encoding='UTF-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    with open('phone.csv', 'w', encoding='UTF-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            if el['Фамилия'] != lst[0] and el['Имя'] != lst[1]:
                f_writer.writerow(el)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'c':
            if not exists('phone.csv'):
                create_file()
            change_file(get_info())
        elif command == 'd':
            if not exists('phone.csv'):
                create_file()
            delete_data(get_info())


main()
