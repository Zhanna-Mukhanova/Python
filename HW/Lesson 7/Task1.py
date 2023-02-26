# 1. пара-ра-рам рам-пам-папам па-ра-па-дам
# # Парам пам-пам

glasnye = "аоуыэяёюие"
words = input().split()
vovel_numbers = [sum(True for j in word if j.lower() in glasnye) for word in words]

if all(vovel_numbers) and len(set(vovel_numbers)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
