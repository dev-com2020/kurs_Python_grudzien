# string = input('Wpisz coś: ')

# upper, lower = 0, 0
# for i in string:
#     if(i.islower()):
#         lower = lower + 1
#     elif(i.isupper()):
#         upper = upper + 1
#
# print('Małe litery:',lower)
# print('Duże litery:',upper)

# tekst = "Matematyka jest królową wszystkich nauk"
# print(tekst.count('m'))
# print(tekst.count('M'))

# tekst = ("Matematyka jest królową wszystkich nauk")
# duzeM = tekst.count("M")
# print(duzeM)
# maleM = tekst.count("m")
# print(maleM)


for v in ['o'] + [' '.join('*' * i) for i in range(3, 10, 2)] + ['|', '|']:
    print('{:~^17}'.format(v))

#
# tekst = ""
# for i in range(9):
#     tekst += "0"
#     print(tekst)
#
# # tekst = "000000000"
# for i in range(9):
#     tekst = tekst[:-1]
#     print(tekst)

# tekst = "O"
# for i in range(9):
#     print(tekst)
#     tekst = tekst + "O"
#
# for i in range(10):
#     print(tekst)
#     tekst = tekst [:-1]

for i in range(1, 10):
    print("o" * i)
for i in range(8, 0, -1):
    print("o" * i)

