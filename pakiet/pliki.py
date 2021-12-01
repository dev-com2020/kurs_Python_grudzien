# uchwytR = open("adresy.txt", "r", encoding="utf-8")
# uchwytW = open("adresy.txt", "w",encoding="utf-8")
#uchwytA = open("adresy.txt", "a", encoding="utf-8")

# uchwyt2 = open(r"C:\users\razor\pong\sprites.py")
# uchwytW.write("Wyniki programu...\nczęść 1")
#uchwytA.write("\nWyniki programu...\nczęść 2")
# dane = uchwytR.read()
# for i in uchwytR:
#     print(i)
# uchwytR.close()
# uchwytW.close()
#uchwytA.close()

try:
    with open("adresy.txt", "r", encoding="utf-8") as uchwyt:
        for i in uchwyt:
            print(i)
except IOError:
    print("Wystąpił problem z plikem, sprawdź nazwę pliku")

input('Wciśnij ENTER aby zakończyć!')