#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет:"))
a = 0
for i in range(n):
    a += int(input("Укажите монету - 0 (орел) или 1 (решка):"))
print(min(a, n - a))