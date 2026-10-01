from random import randint
nimi = input("Nimesi: ")
age = int(input("Ikäsi: "))
l1 = []

def noppaPeli():
            dice = randint(1,6)
            dice1 = randint(1,6)
            print(f"\nHeitettiin {dice} ensimmäisellä nopalla\nHeitettiin {dice1} toisella nopalla\n")

def kolikonheitto():
            coin = randint(1,2)
            if coin == 1:
                print(f"\nHeitettiin kruuna")
            else:
                print(f"\nHeitettiin klaava")
def getItem():
    item = input("Minkä esineen haluat lisätä? ").lower()
    l1.append(item)
    print(f"Lisättiin {item} inventaarioon")
def usePotion():
    if "potion" in l1:
        l1.remove("Potion")
        print("Käytit potionin")
    else:
        print("Sinulla ei ole potionia")
def showInventory():
      print("\nTavaraluettelosi:\n")
      for i in l1:
            print(f"{i}")
while True:

    if age < 12:
        print("Olet alaikäinen. Peli sammuu.")
        break
    else:
        print(f"\nNimesi on {nimi} ja olet {age}-vuotias\nVALIKKO\n1. Heitä noppaa\n2. Heitä kolikkoa \n3. Hommaa tavara\n4. Käytä potion\n5. Näytä inventory\n6. Lopeta peli")
        selection = int(input("\nValintasi: "))
        if selection == 1:
                noppaPeli()
        elif selection == 2:
            kolikonheitto()
        elif selection == 3:
              getItem()
        elif selection == 4:
              usePotion()
        elif selection ==5:
              showInventory()
        elif selection == 6:
            print("Peli lopetetaan")
            break



