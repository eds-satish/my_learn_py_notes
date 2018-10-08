import re
import xml.etree.ElementTree as ET

reg1 = re.compile(r"{\w.*?}")


tree = ET.parse('/root/mypython-root/test-dir/conff.xml')
root = tree.getroot()

"""
#print(type(tree), type(root))
print(root.tag, root.attrib)

#to iterate over the child element (after root element)
#for child in root:
#    print(child.tag, child.attrib)

#gives you a single list output of all the elements
print([child.tag for child in root.iter()])
print([child.attrib for child in root.iter()])

ctag = [child.tag for child in root.iter()]
cattr = [child.attrib for child in root.iter()]
ctxt = [child.text for child in root.iter()]
ctail = [child.tail for child in root.iter()]

print(ctag[0], cattr[0], sep=' : ')

for i in range(len(ctag)):
    print(ctag[i], cattr[i], ctxt[i], ctail[i], sep=' : ')

"""

#to iterate over all the child elements (all the tags it will go through)
for ele in root.iter():
#    print(ele.tag, ele.attrib, ele.text, ele.tail)
    tup = ele.tag, ele.attrib, ele.text, ele.tail
    #print(list(tup))
    ll = list(tup)
    #ll.pop(0)
    print(ll)
    


#prints the complete XML file for us **imp** when needed to copy
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

"""
#printing only one of the node/element 'neighbor'
for child in root.iter('neighbor'):
    print(child.tag, child.attrib, child.text, child.tail)

#for quickly find the element and attribute of a given child when it is of 'text' type
for child in root.findall("./country/[year='2008']"):
    print('findall-1: ', child.tag, child.attrib, child.text)

#for quickly find the element and attribute of a given child when it is of 'attribute' type
for child in root.findall("./country/neighbor[@direction='W']"):
    print('findall-2: ', child.tag, child.attrib)
"""


