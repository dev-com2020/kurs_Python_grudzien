import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

print(lista)
print("Suma=", sum(lista))
print("Średnia wartość=", sum(lista) / len(lista))
