# def mnozenie(a, b):
#     try:
#         return a * b
#     except TypeError:
#         return 0

# print(mnozenie("4","a"))
import logging


def mnozenie(a, b):
    '''
    :param a: int
    :param b: int
    :return: mnożenie liczb całkowitych
    :raises TypeError: W przypadku, gdy parametry nie będą liczbami
    '''
    return int(a) * int(b)


# try:
#     print(mnozenie(None, 3))
# except (TypeError, ValueError):
#     logging.warning('Niedozwolona operacja!')


# try:
#     from pakiett import *
# except ImportError:
#     print("Błąd importu pakietu!")

#
# try:
#     print(mnozenie('4', 3))
# except TypeError:
#     logging.warning('Błąd typu danych!')
# except ValueError:
#     logging.warning('Niedozwolona wartość!')
# else:
#     imie = input("Podaj imie")
#     print(imie)
# finally:
#     print("I tak się wykonam!")

def wiek(users, age):
    try:
        return _wiek(users, age)
    except:
        print("Niepoprawne dane!")
    return 0


def _wiek(users, age):
    count = 0
    for user in users:
        if int(user['age']) < age:
            count += 1
    return count
