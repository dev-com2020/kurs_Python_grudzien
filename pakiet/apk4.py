from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x500')
ws.resizable(0,0)

frame = Frame(ws, height=500, width=400, bg='green')
frame.pack()



# Checkbutton(food, text='Pizza').pack(anchor=W)
# Checkbutton(food, text='Noodles').pack(anchor=W)
# Checkbutton(food, text='Sandwich').pack(anchor=W)
# Checkbutton(food, text='eggs').pack(anchor=W)
#
# drinks = LabelFrame(frame, text='Drinks', bd=5, relief=RIDGE)
# drinks.grid(row=0, column=1, sticky=E, padx=20, pady=20)
#
# Checkbutton(drinks, text='Water').pack(anchor=W)
# Checkbutton(drinks, text='Coffee').pack(anchor=W)
# Checkbutton(drinks, text='Fanta').pack(anchor=W)
# Checkbutton(drinks, text='Bear').pack(anchor=W)

ws.mainloop()