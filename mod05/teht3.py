l1 = []
while True:
    number = (input("luku: "))
    if number == "":
        print(f"Pienin luku: {min(l1)}")
        print(f"Suurin luku: {max(l1)}")
        break
    number = int(number)
    l1.append(number)
