class Czlowiek:

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Cześć, mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się uczę!")
        else:
            print("2+2-3*6...")


cz1 = Czlowiek("Tomek", 38, "m")
print("Obiekt cz1=", cz1.imie, cz1.wiek, cz1.plec)
cz1.przywitaj()
cz1.ruszaj()
cz1.mysl()

cz2 = Czlowiek("Ewa", 18, "k")
print("Obiekt cz2=", cz2.imie, cz2.wiek, cz2.plec)
cz2.przywitaj()
cz2.ruszaj()
cz2.mysl()
