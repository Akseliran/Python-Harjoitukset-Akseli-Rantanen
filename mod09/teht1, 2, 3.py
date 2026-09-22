class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettuMatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettuMatka = kuljettuMatka
    def kiihdytä(self, accel):
        self.nopeus += accel
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, x):
        self.kuljettuMatka += self.nopeus*x


    

auto1 = Auto("ABC-123", 142)

print(f"Auton reksiteritunnus on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus}")
while True:

    tes = int(input("Paljonko haluat kiihdyttää? "))
    auto1.kiihdytä(tes)
    print(f"Auto kulkee {auto1.nopeus}km/h ja on kulkenut {auto1.kuljettuMatka}km")
    

