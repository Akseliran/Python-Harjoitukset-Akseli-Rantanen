import random

randomNumber = random.randint(1, 10)
while True:
    guess = int(input("Arvaa luku väliltä 1-10: "))
    if guess == randomNumber:
        print("Oikein!")
        break
    elif guess < randomNumber:
        print("Liian pieni luku, yritä uudelleen.")
    elif guess > randomNumber:
        print("Liian suuri luku, yritä uudelleen.")
       