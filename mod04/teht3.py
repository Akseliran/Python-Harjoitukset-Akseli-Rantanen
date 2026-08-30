gender = input("Sukupuoli: (Mies tai Nainen)\n").lower()
if gender == "mies" or gender == "nainen":
    hemo = float(input("Hemoglobiiniarvo (g/l):\n"))
    if gender == "nainen":
        if  117 < hemo < 175:
            print("Normaali")
        elif hemo > 175:
            print("Korkea")
        elif hemo < 117:
            print("Matala")
        else:
            print("Invalid value")        
    else:
        if 134 < hemo < 195:
            print("Normaali")
        elif hemo > 195:
            print("Korkea")
        elif hemo < 134:
            print("Matala")
        else:
            print("Invalid value") 
else:
    print("Invalid gender")
    