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

    def __init__(self, szybkosc=150):
        super().__init__("Orzeł bielik", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, "rozpoczynam polowanie")

    def wydajOdglos(self):
        print("grrrrr")


class Kura(Ptak):

    def __init__(self):
        super().__init__("Kura Zosia", 0)

    def znosiJajko(self):
        print("Tu", self.gatunek, "właśnie znoszę jajko!")

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam!")

    def wydajOdglos(self):
        print("kokoko")


o = Orzel(99)
k = Kura()
o.lataj()
o.poluj()
o.wydajOdglos()
k.lataj()
k.wydajOdglos()
k.znosiJajko()

# tak nie róbmy!!! :)
# for i in range(3):
#     print(i)
# else:
#     print("!!!!")

# a = 4
# b = 9
#
# for i in range(2, min(a, b) + 1):
#     print('Sprawdzanie!', i)
#     if a % i == 0 and b % i == 0:
#         print('To nie jest liczba pierwsza!')
#         break
# else:
#     print('Liczba pierwsza :)')
