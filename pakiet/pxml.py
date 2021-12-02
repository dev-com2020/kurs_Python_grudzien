from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('produkt')
productChild.setAttribute('nazwa', 'Kurs Python')

xml.appendChild(productChild)
xml_str = root.toprettyxml(indent="\t")

save_path = "produkt.xml"

with open(save_path, "w") as f:
    f.write(xml_str)
