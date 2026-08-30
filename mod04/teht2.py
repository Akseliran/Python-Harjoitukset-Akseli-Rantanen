selection = input("Mistä hyttiluokasta haluat kuulla sanallisen kuvauksen?\nLUX, A, B vai C Kirjoita tähän:\n").upper()
if selection == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif selection == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif selection == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif selection == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")