import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

print(lista)
print("MIN:", min(lista))
print("MAX:", max(lista))

# a = int(input("Podaj liczbę: "))
#
# if a < 11:
#     print("Mała liczba")
# elif 9 < a < 100:
#     print("To jest liczba z przedziału 9 do 100")


# if a in lista:
#     print("Liczba", a, "znajduje się na liście")
# else:
#     print("Liczba", a, "nie znajduje się na liście")

# if a == 0:
#     print("Liczba jest zerem!")
# elif a > 0:
#     print("Liczba jest większa od zera")
# else:
#     print("Nie wiem jaka to liczba?")
