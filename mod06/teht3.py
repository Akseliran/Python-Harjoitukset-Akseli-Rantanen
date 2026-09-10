number = int(input("luku: "))
if number == 2:
    print(f"luku ei ole alkuluku")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"luku ei ole alkuluku")
            break
    else:
        print(f"luku on alkuluku")