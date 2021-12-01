def triangle(n):
    for i in range(n):
        for j in range(n - i):
            print(' ', end=' ')
        for k in range(2 * i + 1):
            print('*', end=' ')
        print()


def shape(n):
    for i in range(n):
        for j in range(n - 1):
            print(' ', end=' ')
        print('* * *')

r = int(input("Podaj ilość wierszy"))
triangle(r)
triangle(r)
shape(r)
input('Wciśnij ENTER aby zakończyć program!')