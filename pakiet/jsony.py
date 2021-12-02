import json


with open('imiona.json') as f:
    katalog_dict = json.load(f)

print(json.dumps(katalog_dict, indent="\t", sort_keys=True))


# print(katalog_dict)
#
# kody = {"Kielce": 25-900,
#         "Warszawa": 00-900,
#         "Lublin": 34-200,
#         }
#
# with open('kody.txt',"w") as jsonP:
#         json.dump(kody,jsonP)


# to_json = json.dumps(kody)
#
# print(to_json)