import random

ranNumber = random.randint(1, 100)
guess = 0
attempts = 0
helpTime = 0


while guess != ranNumber:
    if attempts % 10 == 0 and attempts > 1:
        select = input("Do you want a hint?. (y/n)").lower()
        if select == "y":
            if ranNumber % 2 == 0:
                print("The number is even")
            else:
                print("The number is odd")
    attempts +=1
    guess = int(input("Guess the number: "))
print(f"you got the number correct in {attempts} tries!\n The odds of that are {1-((1-0.01)**attempts):.3f}!")