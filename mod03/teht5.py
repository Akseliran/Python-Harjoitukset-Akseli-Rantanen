luodValue = 13.3
naulValue = 32*luodValue
leivValue = 20*naulValue

leivAmount = int(input("Anna leiviskät\n"))
naulAmount = int(input("Anna naulat\n"))
luodAmount = int(input("Anna luodit\n"))

total = luodValue*luodAmount+naulValue*naulAmount+leivValue*leivAmount
kg=int(total // 1000)
g=total % 1000
print(f"Massa nykymittojen mukaan:\n{kg} kilogrammaa ja {g :.2f} grammaa")