lista = [i for i in range(10)]
print(lista)

slownik = {1: "Tomek", 2: "Kacper", 3: "Anna"}
print({value: key for key, value in slownik.items()})
print(slownik)

lista1 = [1, 2, 2, 3, 4, 4, 5]
zbior = {i for i in lista1}
print(zbior)
