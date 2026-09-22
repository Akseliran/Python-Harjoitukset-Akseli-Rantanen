from random import randint
autot = []

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


#autot luodaan
for i in range(10):
    autot.append(Auto(f"ABC-{i} ", randint(100, 200)))

voittaja = 0
while voittaja == 0:
    #itse kilpailun funktiot  
    for auto in autot:
        auto.kiihdytä(randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettuMatka >= 10000:
            voittaja = auto
print(f"{voittaja.rekisteritunnus} on voittaja!")

