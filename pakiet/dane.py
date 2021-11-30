# imie = input("Podaj imię: ")
# wiek = input("Podaj wiek: ")
# print('Twoje imię:', imie, ",a twój wiek:", wiek)

# a = input("Podaj liczbę a: ")
# b = int(input("Podaj liczbę b: "))
# print(type(a))
# print("Suma liczb wynosi: ", int(a) + b)

imie = "Tomek"
nazwisko = "Kowalski"

# print(imie.upper())
# print(imie.lower())
# print(imie.count("ek"))
# print(len(nazwisko))
#
#
# print(imie[0])
# print(imie[-1])
# print(imie[0:3])
#
# print(imie+" "+nazwisko[0]+".")

# deklaracja = "Lubię %s"
# co_lubie = input("Napisz co lubisz:")
# print(deklaracja % "cukierki")
# print("Lubię %s, oraz programować" % co_lubie)

# %s oznacza, że w miejsce tego znacznika będzie podstawiany ciąg tekstowy
# %i - to liczba całkowita
# %f - liczba rzeczywista lub inaczej zmiennoprzecinkowa


# print("moja wersja Pythona to: %i" % 3)
# print("a dokładniej: %f" % 3.8)
# print("a w przybliżeniu: %.1f" % 3.8)
# print("a w przybliżeniu: %.f" % 3.8)

print("Lubię język {1} oraz {0}".format("Python", "Java"))
print(f"Lubię język {imie} oraz {nazwisko}")
print("Lubię %(jezyk)s" % {"jezyk": "Pythona"})

