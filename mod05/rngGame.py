import random

ranNumber = random.randint(1, 100)
guess = 0
attempts = 0
helpTime = 0

def help():
    global helpTime
    if helpTime == 0:
        helpInt = 50
    elif helpTime == 1:
        helpInt = 75
    helpTime +=1
    if ranNumber <= helpInt:
        print(f"The number is lower than {helpInt+1}")
    else:
        print(f"The number is higher than {helpInt-1}")

while guess != ranNumber:
    if attempts % 10 == 0 and attempts > 1 and helpTime < 2:
        select = input("Do you want a hint?. (y/n)").lower()
        if select == "y":
            help()
    attempts +=1
    guess = int(input("Guess the number: "))
print(f"you got the number correct in {attempts} tries!\n The odds of that are {1-((1-0.01)**attempts):.3f}!")