# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s, p = map(int, input("Введите сумму и произведение чисел через пробел:").split())
a, b = 0, 0
for x in range(s):
    for y in range(s):
        if s == x + y and p == x * y:
            a, b = x, y
print(f'x равен "{a}", y равен "{b}"')
