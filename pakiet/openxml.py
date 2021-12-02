from xml.dom import minidom

DOMTree = minidom.parse('produkt.xml')

cNodes = DOMTree.childNodes

print(cNodes[0].getElementsByTagName("produkt")[0].nodeName)
print(cNodes[0].getElementsByTagName("produkt")[0].childNodes[0].toxml())
print(cNodes[0].getElementsByTagName("produkt")[0].getAttribute("nazwa"))
