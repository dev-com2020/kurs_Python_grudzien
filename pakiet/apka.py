from tkinter import *
from tkinter.ttk import Combobox


def click():
    # print("Kliknięto!")
    zmienna = "Witaj " + txt.get()
    lbl.configure(text=zmienna)


####################################################################

window = Tk()
window.title("Witamy w aplikacji!")
window.geometry('400x250')
lbl = Label(window, text="Witaj!", font=("Arial Bold", 20), fg="red")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10, state='disabled')
txt.grid(column=1, row=0)
btn = Button(window, text='Kliknij!', bg="green", fg="white", command=click)
btn.grid(column=1, row=1)
combo = Combobox(window)
combo['values'] = ('jeden', 'dwa', 'trzy')
combo.grid(column=1, row=2)
# chk_state = BooleanVar()
# chk_state.set(False)
chk_state = IntVar()
chk_state.set(1)
chk = Checkbutton(window, text="Wybierz:", var=chk_state)
chk.grid(column=1, row=3)
rad1 = Radiobutton(window, text="pierwszy", value=1)
rad2 = Radiobutton(window, text="drugi", value=2)
rad3 = Radiobutton(window, text="trzeci", value=3)
rad1.grid(column=2, row=0)
rad2.grid(column=2, row=1)
rad3.grid(column=2, row=2)

window.mainloop()
