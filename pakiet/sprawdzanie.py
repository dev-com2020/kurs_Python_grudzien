def szukaj(tekst, znak):
    for i in tekst:
        if i == znak:
            print("Znalazłem szukany znak", znak)
            return
    print("Nie znalazłem szukanego znaku", znak)


#zmienna = input("Podaj tekst:")
# szukaj(zmienna, "a")

def szukanie():
    string = input("podaj stringa: ")
    znak = input("podaj znak: ")
    if string.count(znak) > 0:
        print("string zawiera znak " + znak)
    else:
        print("string nie zawiera znaku " + znak)


#szukanie()


# wyszukiwanyZnak = input("Podaj wyszukiwany znak\n")
# znaki = input("Podaj łańcuch znaków\n ")
#
# for i in znaki:
#     if znaki.__contains__(wyszukiwanyZnak):
#         print("wyszukiwany znak występuje: " + wyszukiwanyZnak)
#         break
#     else:
#         print("wyszukiwany znak nie występuje")


# sprawdzam = "TTEEST"
#
# out = {x: sprawdzam.count(x) for x in set(sprawdzam)}
#
# print("Liczba poszczególnych znaków :\n " + str(out))

# tekst=""
# znak=""

def przeszukanie(tekst,znak):

    for i in tekst:
        if i == znak:
            print("znalazlem",znak)
            return
        print("nie znalazlem",znak)

tekst=input("Podaj tekst:\n")
znak=input("Podaj znak:\n")

przeszukanie(tekst,znak)
