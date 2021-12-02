import csv
#
# with open('trade.csv', 'w') as f:
#     writer = csv.writer(f,delimiter='\t')
#     dane = [['WTSQ.QQZ9CT,2021.12,12846.985,,E,Funty,0,Wholesale Trade Survey - WTS,Industry by variable - (ANZSIC06) - Subannual Financial Collection,Total wholesaling,Total stocks,Current prices,Trend'],
#             ['ETWQ.TQV9CT,2022.02,12846.985,,F,Złotówki,9,Wholesale Trade Survey - WTS,Industry by variable - (ANZSIC06) - Subannual Financial Collection,Total wholesaling,Total stocks,Current prices,Trend']]
#     writer.writerows(dane)

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for i in reader:
        print(i)

