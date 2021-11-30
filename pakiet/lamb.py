# lambda parametr: wyrażenie

# dodawanie = lambda x, y: x + y
#
# print(dodawanie(2, 3))
# print((lambda x, y: x + y)(2, 3))
from functools import reduce


def funkcja(f, liczba):
    return f(liczba)


# def dodaj(x):
#     return x + 1
#
# def kwadrat(par):
#     return par * par


# print(funkcja(lambda x: x + 1, 7))
# print(funkcja(lambda x: x * x, 7))
#

# lista = [1, 3, 5, 7]
#
# print(f"Nasza lista:{lista}\n")
# print(f"Zastosowanie map: {list(map(lambda _: _ * 2, lista))}")
# print(f"Zastosowanie filter: {list(filter(lambda _: _ > 3, lista))}")
# print(f"Zastosowanie reduce: {reduce(lambda x, y: x + y, lista)}")

