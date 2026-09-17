tup = (3,5,8,10,(24,25),"moi",200)

print(len(tup))

print(tup.index(10))

if 10 in tup:
    print("tupissa on luku 10")
elif 210 in tup:
    print("tupissa on luku 210")
else:
    print("tupissa ei ole lukuja 10 tai 210")

for i in tup:
    print(i)
    
tup1 = tup[::-1]

print(tup1)


