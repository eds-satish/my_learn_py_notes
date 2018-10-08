#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import re
import urllib

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print(soup.prettify())
# <html>
#  <head>
#   <title>
#    Page title
#   </title>
#  </head>
#  <body>
#   <p id="firstpara" align="center">
#    This is paragraph
#    <b>
#     one
#    </b>
#    .
#   </p>
#   <p id="secondpara" align="blah">
#    This is paragraph
#    <b>
#     two
#    </b>
#    .
#   </p>
#  </body>
# </html>





#page = urllib3.urlopen("http://www.icc-ccs.org/prc/piracyreport.php")
page = urllib.request.urlopen("http://www.icc-ccs.org/prc/piracyreport.php")
print(page)
soup = BeautifulSoup(page)
for incident in soup('td', width="90%"):
    where, linebreak, what = incident.contents[:3]
    print(where.strip())
    print(what.strip())
    print()

