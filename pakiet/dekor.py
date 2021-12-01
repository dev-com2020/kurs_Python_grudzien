import calendar
import time


def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się!", koniec - start, 'sekund.')
        return x

    return wew


@dekor
def policz(a, b):
    time.sleep(3)
    print("Wynik:", a + b)


@dekor
def policz2(a, b, c):
    time.sleep(1.5)
    print("Wynik:", a + b * c)


# policz(4, 3)
# policz2(4, 3, 5)

# czas = time.strftime("%Y-%m-%d")
# print(czas)
# time = time.strptime("2021 12 01","%Y %b %d")
# print(time)

kal = calendar.month(2021, 12)
print(kal)
