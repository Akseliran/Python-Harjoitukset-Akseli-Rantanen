def removeOdds(list):
    l2=[]
    for i in list:
        if i % 2 == 0:
            l2.append(i)
    return l2


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Listan parilliset luvut ovat: {removeOdds(l1)}")