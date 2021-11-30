liczby = list(range(1, 10, 2))
print(liczby)
for i in liczby:
    print(i)

index = 0
while index < len(liczby):
    print("Liczby[", index, "]= ", liczby[index])
    index += 1
print("Długość listy: ", len(liczby))
