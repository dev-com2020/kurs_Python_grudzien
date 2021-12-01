from tkinter import *

window = Tk()
window.title("Witamy w aplikacji!")

for fm in ['blue', 'red', 'green', 'black', 'white']:
    Frame(height=20, width=400, bg=fm).pack()
mainloop()
