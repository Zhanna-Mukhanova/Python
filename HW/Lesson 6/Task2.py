# 2. пара-ра-рам рам-пам-папам па-ра-па-дам
# Парам пам-пам

num_list = [int(i) for i in input().split()]
num_min = int(input())
num_max = int(input())

print([ind for ind, val in enumerate(num_list) if num_min <= val <= num_max])
