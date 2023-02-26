# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
# Пример:
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

n = int(input())
m = int(input())

massive1 = [int(i) for i in input().split()]
if len(massive1) != n:
    print("Error. Massive1 length is not as noted ")
massive2 = [int(m) for m in input().split()]
if len(massive2) != m:
    print("Error. Massive2 length is not as noted ")
else:
    print(*sorted(set(massive1).intersection(massive2)))
