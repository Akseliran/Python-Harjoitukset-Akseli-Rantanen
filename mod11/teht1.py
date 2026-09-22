class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sivumäärä {self.sivumäärä}, Kirjoittaja {self.kirjoittaja}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)


aku_ankka.tulosta_tiedot()
hytti_no6.tulosta_tiedot()