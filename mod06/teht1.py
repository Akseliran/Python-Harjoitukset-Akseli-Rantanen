import random
times = int(input("Anna heittojen määrä: "))
summa = 0
for i in range(times):
    dice1 = random.randint(1, 6)
    summa += dice1

print(f"heittojen summa: {summa}")