# licznik = 0
# while True:
#     licznik += 1
#     print(licznik)
#     if licznik > 10:
#         break

lista = []
print("\tPodaj liczby,\naby zakończyć wpisz \\stop\\.")
while True:
    wejscie = input("Podaj liczby:\n")
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))

print("Twoja lista ->",lista)
