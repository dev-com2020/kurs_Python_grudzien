import sqlite3

conn = sqlite3.connect('example.sqlite')

c = conn.cursor()

for i in c.execute('SELECT * FROM transakcje ORDER BY cena'):
    print(i)


# c.execute('''
#             CREATE TABLE transakcje
#             (data TEXT,id INTEGER, cena REAL)
#             ''')
#
# c.execute('''
#             INSERT INTO transakcje VALUES
#             ('2021-12-02',1,19.99)
#             ''')

#c.execute('''
            # INSERT INTO transakcje VALUES
            # ('2021-12-01',2,39.99)
            # ''')

#conn.commit()
conn.close()



















# import time
#
#
# class Zegar:
#     def podaj_czas(self):
#         print(time.strftime('%H:%M', time.gmtime()))
#
#
# zegar = Zegar()
#
# zegar.podaj_czas()


# a = 0
# b = 9
# try:
#     if a <= 0 or b <= 0:
#         raise ZeroDivisionError("Wartości są zerowe lub ujemne")
#     print('wynik dzielenia:=', a / b)
# except ZeroDivisionError:
#     raise

'''
AttributeError	This exception occurs when the attribute that we are tryinh to access(whether for assigning a value or getting a value) doesn't exists. For example: Trying to access a class member variable which is not defined in class.
ImportError	This exception occurs when the imported module is not found.
IndentationError	This exception occurs when there is some issue with the code indentation.
TypeError	When an operation is executed on a variable of incorrect type.
ValueError	When for a function, argument value is incorrect.
ZeroDivisionError	As discussed above, when we try to divide a number with zero.
TabError	When the indentation is not consistenet throughout the code in terms of tabs and spaces used for indentation.
RuntimeError	When an error is not of any specific defined exception type, python calls it RuntimeError.
NameError	When a variable name we are trying to use is not defined.'''


