# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

print("Введите натуральное число N")
n = int(input())
lst = []
import random

for i in range(n):
    lst.append(random.randint(1, n))
print(lst)

print("Введите число X")
x = int(input())
min_diff = abs(x - lst[0]) # Функция abs() возвращающая абсолютное значение числа
imd = 0
for i in range(1, n):
    if abs(x - lst[i]) < min_diff:
        min_diff = abs(x - lst[i])
        imd = i
print(lst[imd])


