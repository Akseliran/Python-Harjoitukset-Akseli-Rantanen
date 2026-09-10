l1 = []
while True:
    number = (input("luku: "))
    if number == "":
        l1.sort(reverse=True)
        print(f"listan viisi suurinta lukua: {l1[0:5]}")
        break
    number = int(number)
    l1.append(number)
