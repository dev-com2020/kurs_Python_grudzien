from zipfile import *

with ZipFile("archiwum.zip", 'w') as z:
    z.write("produkt.xml")
    z.write("produkt.json")
    z.close()

with ZipFile("archiwum.zip", 'r') as z:
    print(z.namelist())
    z.extractall()
    z.close()