from random import randint


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
class kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = []
        for i in range(autot):
            self.autolista.append(Auto(f"ABC-{i} ", randint(100, 200)))
    def tunti_kuluu(self, x):
        for auto in self.autolista:
            auto.kiihdytä(randint(-10, 15))
            auto.kulje(x)
    def tulosta_tilanne(self):
        for auto in self.autolista:
            print(f"auto: {auto.rekisteritunnus} | kuljettu matka: {auto.kuljettuMatka}")
        print("-"*30)
    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettuMatka >= self.pituus:
                    self.voittaja = auto
                    return True
        return False


comp = kilpailu("Suuri Romuralli", 8000, 10)
tuntejakulunut=0
while comp.kilpailu_ohi() == False:
    comp.tunti_kuluu(1)
    tuntejakulunut+=1
    if tuntejakulunut % 10 == 0:
        print(f"{tuntejakulunut} tuntia kulunut")
        comp.tulosta_tilanne()
print(f"Kilpailu ohi {tuntejakulunut} tunnin jälkeen")
comp.tulosta_tilanne()

print(f"{comp.voittaja.rekisteritunnus} on voittaja!")

