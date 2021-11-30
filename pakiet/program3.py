imiona = ['Jakub', 'Tomek', 'Kacper','Tomek']
print("Pierwsza wersja listy:", imiona)

imie = input("Które imię mam zmienić?\n")
imie_index = imiona.index(imie)
nowe_imie = input("Podaj nowe imię:\n")

imiona[imie_index] = nowe_imie
print("Druga wersja listy:", imiona)
