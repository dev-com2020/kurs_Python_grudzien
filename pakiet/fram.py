from tkinter import *

window = Tk()
window.title("Witamy w aplikacji!")
#window.geometry('400x250')

tl = Label(window, text="Tekst", justify=LEFT, padx=10)
tl.pack(side=TOP)

obraz = PhotoImage(file='LOGO_DEVC.png')
obraz = obraz.subsample(3)
imgL= Label(window,image=obraz)

imgL.pack(side=RIGHT)

mainloop()