# 1. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(n, m):
    if n == 0:
        return n
    if n < 0:
        return power(n, m + 1) / n
    if n > 0:
        return power(n, m - 1) * n


n = int(input())
m = int(input())

print(power(n, m))
