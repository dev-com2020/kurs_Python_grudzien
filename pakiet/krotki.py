# krotka = (1, 4.56, "Tomek")
# # trik, raczej nie stosujemy
# nowa_lista = list(krotka)
# print(type(nowa_lista))
#
# # zbiór/set
# ocenyJanka = {1, 2, 3.5, 4, 5.43, 6}
# ocenyKacpra = {1, 2, 3.5, 7}
# print(ocenyJanka)
# oceny.add(5)
# oceny.add("5")
# oceny.add("2")
# oceny.add("Tomek")
# oceny.add(7)
# oceny.add(17)
# oceny.add(-17)
# print(ocenyJanka.difference(ocenyKacpra))
# print(ocenyJanka.intersection(ocenyKacpra))
# print(ocenyJanka - ocenyKacpra)
# print(ocenyJanka | ocenyKacpra)
# print(ocenyKacpra & ocenyJanka)
# print(ocenyJanka)
# print(ocenyKacpra)

def srednia(a, b):
    return (a + b) / 2.0


(a, b) = (1.2, 4.5)

print("Średnia z dwu liczb:", "a=", a, "b=", b, "wynosi:", srednia(a, b))
