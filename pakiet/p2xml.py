import xml.etree.ElementTree as et


def generate_xml(fileName):
    root = et.Element("Katalog")

    m1 = et.Element('Procesor')
    root.append(m1)

    b1 = et.SubElement(m1, 'marka')
    b1.text = 'Intel'

    b2 = et.SubElement(m1, 'marka')
    b2.text = 'AMD'

    m2 = et.Element('RAM')
    root.append(m2)

    b3 = et.SubElement(m2, 'marka')
    b3.text = 'Intel'

    b4 = et.SubElement(m2, 'marka')
    b4.text = 'GoodRam'

    m3 = et.Element('Cena')
    root.append(m3)

    b5 = et.SubElement(m3, 'kwota')
    b5.text = '300'

    b6 = et.SubElement(m3, 'waluta')
    b6.text = 'PLN'

    tree = et.ElementTree(root)
    with open(fileName,'wb') as f:
        tree.write(f)

generate_xml('Katalog.xml')

