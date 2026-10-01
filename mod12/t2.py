import t1

with open("tallennalista.json", "w") as tiedosto:
    t1.dump(t1.li1, tiedosto)