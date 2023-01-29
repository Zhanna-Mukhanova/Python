"""Найдите сумму цифр трехзначного числа.
in 123
out 6

in 100
out 1
"""

num = int(input())
result = 0
num1 = num % 10
num2 = num % 100 // 10
num3 = num // 100
result = num1 + num2 + num3
print(result)
