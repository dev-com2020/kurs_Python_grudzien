from tkinter import *
from tkinter import scrolledtext, messagebox, ttk
from tkinter.ttk import Progressbar


def click():
    print(wybrany.get())
    # messagebox.showinfo('Tytuł okna', 'Treść okna')
    # messagebox.showerror('Tytuł okna', 'Treść okna')
    # messagebox.askquestion('Tytuł okna', 'Treść okna')
    # messagebox.askyesno('Tytuł okna', 'Treść okna')
    # messagebox.askokcancel('Tytuł okna', 'Treść okna')
    # messagebox.askretrycancel('Tytuł okna', 'Treść okna')
    messagebox.askyesnocancel('Tytuł okna', 'Treść okna')


####################################################################

window = Tk()
window.title("Witamy w aplikacji!")
window.geometry('600x250')
wybrany = IntVar()
wybrany.set(3)
# txt = scrolledtext.ScrolledText(window, width=30, height=10)
# txt.insert(INSERT, 'tutaj jakiś tekst......')
# txt.delete(1.0, END)

rad1 = Radiobutton(window, text="pierwszy", value=1, variable=wybrany)
rad2 = Radiobutton(window, text="drugi", value=2, variable=wybrany)
rad3 = Radiobutton(window, text="trzeci", value=3, variable=wybrany)
btn = Button(window, text='Kliknij!', bg="green", fg="white", command=click)
var = IntVar()
var.set(15)
spin = Spinbox(window, from_=0, to=30, width=5, textvariable=var)

style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar',background='blue')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value']= 50

# txt.grid(column=0, row=0)
btn.grid(column=3, row=1)
rad1.grid(column=1, row=0)
rad2.grid(column=2, row=0)
rad3.grid(column=3, row=0)
spin.grid(column=0, row=2)
bar.grid()

window.mainloop()
