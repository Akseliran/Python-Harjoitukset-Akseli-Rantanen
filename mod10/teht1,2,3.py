class Hissi:
    def __init__(self, alinKerros = 1, ylinKerros = 7):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.kerros = alinKerros
        print("Hissi luotu!")

    def kerros_ylös(self):
        if self.kerros < self.ylinKerros:
            self.kerros += 1
    def kerros_alas(self):
        if self.kerros > self.alinKerros:
            self.kerros -=1
    def siirry_kerrokseen(self, x):
        if self.kerros < x:
            for i in range(x-self.kerros):
                self.kerros_ylös()
        if self.kerros == x:
            pass
        else:   
            for i in range (self.kerros-x):
                self.kerros_alas()
class Talo:
    def __init__(self, alinKerros = 1, ylinKerros = 7, hissiMäärä = 3):
            self.alinKerros = alinKerros
            self.ylinKerros = ylinKerros
            self.hissiMäärä = hissiMäärä
            self.hissilist = []
            for i in range(self.hissiMäärä):
                self.hissilist.append(Hissi(self.alinKerros, self.ylinKerros))

    def ajaHissiä(self, hissiNRO, hissiTargetFloor):
        self.hissilist[hissiNRO].siirry_kerrokseen(hissiTargetFloor)

    def palohälytyts(self):
        for hissi in self.hissilist:
            hissi.siirry_kerrokseen(1)


t=Talo(1,7,3)

t.ajaHissiä(2, 7)
print(f"Hissi 2 on kerroksessa {t.hissilist[2].kerros} ")
t.palohälytyts()
print(f"Hissi 2 on kerroksessa {t.hissilist[2].kerros} ")
#h = Hissi()
#h.siirry_kerrokseen(22)
#print(h.kerros)