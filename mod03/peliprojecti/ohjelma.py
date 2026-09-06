from random import randint
nimi = input("Nimesi: ")
age = int(input("Ikäsi: "))
while True:
    if age < 12:
        print("Olet alaikäinen. Peli sammuu.")
        break
    else:
        print(f"\nNimesi on {nimi} ja olet {age}-vuotias\nVALIKKO\n1. Heitä noppaa\n2. Heitä kolikkoa \n3. Lopeta peli")
        selection = int(input("\nValintasi: "))
        if selection == 1:
                dice = randint(1,6)
                dice1 = randint(1,6)
                print(f"\nHeitettiin {dice} ensimmäisellä nopalla\nHeitettiin {dice1} toisella nopalla\n")
        elif selection == 2:
            coin = randint(1,2)
            if coin == 1:
                print(f"\nHeitettiin kruuna")
            else:
                print(f"\nHeitettiin klaava")
        elif selection == 3:
            print("Peli lopetetaan")
            break



