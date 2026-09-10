while True:
    cm = float(input("Anna pituus senttimetreinä: "))
    inch = 2.54 * cm
    if cm < 0:
        print("Negatiivinen luku, sammutetaan...")
        break
    print(f"Pituus tuumissa: {inch}")