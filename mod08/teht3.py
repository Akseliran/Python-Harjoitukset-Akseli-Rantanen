lentoasemat = {}
while True:
    what = int(input(f"Haluatko syöttää uuden lentoaseman, vai hakea jo syötetyn lentoaseman?\n(1. Syötä uusi lentoasema)\n(2. Hae syötetty lentoasema)\n(3. Lopeta)\n"))
    if what == 1:
        newID = input("Kirjoita uuden lentoaseman ICAO koodi\n")
        newName = input("Kirjoita uuden lentoaseman nimi\n")
        lentoasemat[newID] = newName
        print(f"Uusi lentoasema {newName} asetettu!\n\n")

    if what == 2:
        id = input("Kirjoita haluamasi lentoaseman ICAO koodi\n")
        print(f"Haluamasi lentoasema on {lentoasemat[id]}\n\n")

    if what == 3:
        print(f"\n\n\nSammutetaan...")
        break