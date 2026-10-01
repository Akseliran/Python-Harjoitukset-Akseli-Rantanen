class testi:
    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2
    def print(self):
        print(f"{self.property1} ja {self.property2}")


        

class aliluokka(testi):
    def __init__(self, property1, property2, uusproperty3, uusproperty4):
        super().__init__(property1, property2)
        self.uusproperty3 = uusproperty3
        self.uuspropert4 = uusproperty4
    def tulosta(self):
        super().print()
        print(f"{self.uusproperty3} ja {self.uuspropert4}")

class toinenaliluokka(testi):
    def __init__(self, property1, property2, aliluokkaproperty, aliluokkaproperty2):
        super().__init__(property1, property2)
        self.aliluokkaproperty = aliluokkaproperty
        self.aliluokkaproperty2 = aliluokkaproperty2
    def tulosta(self):
        super().print()
        print(f"tää on toinen aliluokka {self.aliluokkaproperty} ja {self.aliluokkaproperty2}")

t = aliluokka(2, 3, 4, 5)
a = toinenaliluokka(2,8,4,1)
t.tulosta()
a.tulosta()




# assosiaatio on kun kaks luokkaa toimivat toistensa kanssa
# olio on yksi luokan luomista asioista jolla voi olla arvoja

# kapselointi on kun tiedot asetetaan luokalle
# polymorfismi on kun luokalla saadaan monia eri arvoja eri olioiden kautta