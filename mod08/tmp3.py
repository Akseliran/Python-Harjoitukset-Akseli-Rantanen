puhelinumerot = {"Viivi":2434343,
                 "Ahmed":3434343,
                 "Pekka":434343,
                 "George": 4343434}

newUser = input("add a new user: ")
newUserPhone = int(input("New users phone number: "))
puhelinumerot[newUser] = newUserPhone

print(puhelinumerot)