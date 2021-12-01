from tkinter import *


def print(v):
    suwak.config(text='wybrałeś:' + v)


window = Tk()
window.title("Witamy w aplikacji!")
window.geometry('400x250')

suwak = Label(window, bg='white', fg='black', width=20, text='brak')
suwak.pack()

suwak1 = Scale(window, label='Wypróbuj!', from_=0, to=10, orient=HORIZONTAL,
               length=200, showvalue=0, resolution=1, command=print)
suwak1.pack()
window.mainloop()
