vuosi = int(input("Anna vuosi: \n"))
if vuosi % 4 == 0 or vuosi %  100 == 0 and vuosi % 400:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")