from abc import ABC, abstractmethod


class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "startuje i osiągnę prędkośc:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):
    def poluj(self):
        print("Tu", self.gatunek, "rozpoczynam polowanie")
    def wydajOdglos(self):
        print("grrrrr")
class Kura(Orzel):
    def znosiJajko(self):
        print("Tu", self.gatunek, "właśnie znoszę jajko!")

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam!")
    def wydajOdglos(self):
        print("kokoko")


o = Orzel("Orzeł bielik", 80)
k = Kura("Czerwononózka", 10)
o.lataj()
o.poluj()
o.wydajOdglos()
k.lataj()
k.poluj()
k.wydajOdglos()
k.znosiJajko()
