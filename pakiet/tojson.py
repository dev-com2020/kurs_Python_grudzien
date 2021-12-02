import json

import xmltodict

with open("Katalog.xml") as xml:
    data = xmltodict.parse(xml.read())
    xml.close()

    json = json.dumps(data)

    with open("katalog.json", 'w') as json_f:
        json_f.write(json)
        json_f.close()
