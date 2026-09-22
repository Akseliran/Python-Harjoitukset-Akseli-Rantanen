l1 = set("")
name = " "

while name != "":
    name = input("Anna nimi: ")
    if name in l1:
        print("Nimi on jo syötetty")
    else:
        l1.add(name)
for i in l1:
    print(f"{i}")