import random
dice = 1
dice1 = 0
while dice != 3 and dice1 != 3:
    dice = random.randint(1,6)
    dice1 = random.randint(1,6)
    print("NEW THROW\n")
    print(f"rolled {dice} on the first dice\nrolled {dice1} on the second dice\n")
print("Rolled 3 on both dices\nYOU WIN")
