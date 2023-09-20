# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = input("Введите кол-во элементов первого множества:")
m = input("Введите кол-во элементов второго множества:")
list_1 = list()
for i in range(int(n)):
    el = int(input("Введите элементы первого множества:"))
    list_1.append(el)
list_2 = list()
for i in range(int(m)):
    el = int(input("Введите элементы второго множества:"))
    list_2.append(el)
lst_1 = set(list_1)
lst_2 = set(list_2)
print(sorted(lst_1.intersection(lst_2)))
