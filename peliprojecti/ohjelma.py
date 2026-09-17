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
      l1.append("Potion")
      print(f"added a potion to your inventory")
def usePotion():
      l1.remove("Potion")
def showInventory():
      print(f"your inventory: {l1}")

while True:

    if age < 12:
        print("Olet alaikäinen. Peli sammuu.")
        break
    else:
        print(f"\nNimesi on {nimi} ja olet {age}-vuotias\nVALIKKO\n1. Heitä noppaa\n2. Heitä kolikkoa \n3. Hommaa potion\n4. Käytä potion\n5. Näytä inventory\n6. Lopeta peli")
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



