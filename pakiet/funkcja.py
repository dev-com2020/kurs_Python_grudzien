def wydrukuj(tekst="^", ile=1):
    print(tekst * ile)


# wydrukuj(ile=5, tekst="*")

def robie_duzo(ile=0, *args, **kwargs):
    print(ile)
    print(args)
    print(kwargs)


# robie_duzo(imie="Tomasz", wiek=38)

global a
a = 5


def dodaj():
    a = 1
    b = 2
    return a + b


def mnozenie():
    c = 3
    return a * c



