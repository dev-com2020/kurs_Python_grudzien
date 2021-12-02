import pandas as pd

# e = pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names=['Imię', "Nazwisko", 'Wynik'])
# # print(e)
# # e.to_html('test.html')
#
# # zbior = [[1, 2, "Tomek", 4], [44, 55, 66, "Tomek"], [24, "Tomek", 26, 37]]
# # w = pd.DataFrame(zbior)
# # w.columns = ['pierwsza', 'druga', 'trzecia', 'czwarta']
# # print(w)
#
# # kody = {'miasta': ["Kielce", "Warszawa", "Lublin"],
# #         'kody': ['25-900', '00-900', '34-200']}
# #
# # print(pd.DataFrame(kody))
#
# miasta = pd.read_csv('worldcities.csv')
# # print(miasta)
# # miasta.to_html('test2.html')
# # print(miasta.head())
# # print(miasta.tail())
# # print(miasta[0:5])
# # print(miasta.set_index('city'))
# # print(miasta)
# miasta.loc[0, 'city'] = 'Warsaw'
#
# # print(miasta.population.describe())
# # print(miasta.isnull().sum())
# # print(miasta.notnull().sum())
# # print(miasta.duplicated().sum())
# miasta.drop_duplicates()
# #print(miasta[100:200][['city', 'population']])
# # print(miasta.city.unique())
# print(miasta.info())

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium.region.is_unique)
kostium.set_index('region', inplace=True)
# print(kostium)
# print(kostium.loc['Alaska'])

# for index, zawartosc in kostium.iterrows():
#     if zawartosc['4'] == 'Ninja':
#         print(zawartosc['region'])

# print(kostium [ (kostium['2'] == 'Rabbit') | (kostium['3'] == "Pirate")])
# print(kostium [ (kostium['2'] == 'Rabbit') & (kostium['1'] == "Dinosaur")])

kostium['Nowa'] = 'pusto'
# kostium.loc[kostium['1'] == 'Doll','Nowa'] = 'lalka'
print(kostium.rename(columns={'1': 'Pierwsza', '2': 'Druga'}))
# print(kostium)
