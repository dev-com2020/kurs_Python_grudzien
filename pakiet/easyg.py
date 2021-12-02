import easygui
import random

# w= easygui.buttonbox("Czy lubisz język Python?","Zapytanie...",["Oczywiście","Absolutnie NIE","Czasami"])
# easygui.msgbox("Wybrałeś: "+ w)


w = easygui.enterbox("Podaj liczbę: ")
easygui.msgbox("A moja to: " + str(random.randint(1, 100)))
