import random
roll = 0
max_roll = int(input("Nopan tahkojen määrä: "))
def funktio():
    dice = random.randint(1, max_roll)
    print(f"heitettiin {dice}")
    return dice

while roll != max_roll:
    roll = funktio()

