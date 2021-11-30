# for i in range(4, 10, 2):
#     print(i)
#     print("W pętli...")
#
# print("Poza pętlą...")

# for i in range(15, 0, -2):
#     print(i)
#     print("W pętli...")
#
# print("Poza pętlą...")

# liczba = [11, 2, 23]
#
# #suma = 0
#
# for i in liczba:
#     print(i)

# print("Suma: ", suma)

# for i in range(1, 11):
#     if i % 3 == 0:
#         print(i)

# for i in range(1, 11, 2):
#     print(i)

lista = [1, 3, 7, 12]

najmniejsza = 0

for i in lista:
    if najmniejsza > i:
        print(i)
        najmniejsza = i

print("Najmnijesza liczba to: ", najmniejsza)
