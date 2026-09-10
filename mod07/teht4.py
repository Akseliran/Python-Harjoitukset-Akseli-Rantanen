def listanSumma(x):
    summa = 0
    for i in x:
        summa += i
    return summa

l1 = [1, 2, 3, 4, 5]
print(f"Listan summa on {listanSumma(l1)}")