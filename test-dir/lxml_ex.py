from lxml import etree

file_name = "data.xml"
doc = etree.parse(file_name)

for line in doc.xpath('//Line'):
    print("value: ", line.text + ", Id: ", line.attrib["Id"])
