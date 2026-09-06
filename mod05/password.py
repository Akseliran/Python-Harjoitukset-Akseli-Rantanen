password = "admin"
userInput =""
while password != userInput:
    userInput = input("Password: ")
    if password == userInput:
        break
    print("Wrong")

print("Welcome")