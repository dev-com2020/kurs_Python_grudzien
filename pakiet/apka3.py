from tkinter import Label, Button, BOTTOM, LEFT, RIGHT, Tk, Frame

from PIL.Image import Image


def click():
    print("Kliknięto!")


window = Tk()
window.title("Witamy w aplikacji!")
window.geometry('400x250')

# file = filedialog.askopenfilename(initialdir=path.dirname(__file__),filetypes=(("Python", "*.py"), ("Tekstowe", "*.txt")))
# file =filedialog.askdirectory()
#
# menu = Menu(window)
# new_item = Menu(menu,tearoff=0)
# new_item.add_command(label='New',command=click)
# new_item.add_command(label='Koniec')
# menu.add_cascade(label='File',menu=new_item)
# window.config(menu=menu)

# w = Frame(window, width=200, height=200, bg='yellow')
# w.pack()
# bf = Frame(window)
# bf.pack(side=BOTTOM)
# b = Button(w, text='tekst', fg="red")
# b.pack(side=LEFT)
# b2 = Button(w, text='tekst', fg="blue")
# b2.pack(side=RIGHT)
# b3 = Button(w, text='tekst', fg="green")
# b3.pack(side=LEFT)
# b1 = Button(bf, text='tekst1', fg='blue')
# b1.pack(side=BOTTOM)

obraz = Image.open("LOGO_DEVC.png")
obraz.resize((100, 100))
lbl = Label(window, image=obraz)
lbl.pack()

# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='Pierwszy')
# tab_control.add(tab2, text='Drugi')
# lbl1 = Label(tab1, text="Treść 1")
# lbl2 = Label(tab2, text="Treść 2")
# lbl1.grid(column=0, row=0)
# lbl2.grid(column=0, row=0)
# tab_control.pack(expand=1, fill='both')
window.mainloop()
