print ( "Folosim functia search din regexp ne ajuta sa cautam daca un text (la-nceput) se gaseste in alt text \n\n " )
import re
paternuri = [ 'aici' , 'acolo' ]
text = 'aici invatam Python regular expresion, pe care le putem folosi acolo in exercitii'

for patern in paternuri:
    print ( 'Cautam paternul "%s" in textul "%s" -> ' % (patern, text))

    if re.search(patern, text): print ( "se potriveste" )
    else : print ( "nu se potriveste" )

print ( "\n\n re search - pentru a afla pozitia de potrivire \n\n" )

paternuri = 'aici'
text = 'aici invatam Python regular expresion, pe care le putem folosi acolo in exercitii, aici putem invata'

potrivire = re.search(paternuri, text)
start = potrivire.start()
end = potrivire.end()

print (start)
print (end)
print ( 'Gasim "%s" in "%s" de la %d pana la %d ("%s")' % \
        (potrivire.re.pattern, potrivire.string, start, end, text[start:end]))

import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print ( 'Found "%s"' % match)
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    print ( 'Found "%s" in textul de mai sus la pozitia "%d"' % (match.group(), match.start()))

import re
text = 'Acesta este un text unde o sa cautam un cuvant text in tot textul.'
pattern = re.compile( r'\b\w*text\w*\b' )

print ( 'Text:' , text)
pos = 0
while True :
    match = pattern.search(text, pos)
    if not match: break
    s = match.start()
    e = match.end()
    print ( ' %2d : %2d = "%s"' % (s, e- 1 , text[s:e]))
    pos = e

import re

line = "Aici la curs invatam Python"
searchObj = re.search( r'(.*) invatam (.*)' , line, re.M|re.I)
if searchObj:
    print ("searchObj.group() : ", searchObj.group())
    print ("searchObj.group(1) : ", searchObj.group( 1 ))
    print ("searchObj.group(2) : ", searchObj.group( 2 ))
else :
    print("Nothing found!!")

import re

matchObj = re.match( r'a' , 'bcdefa' )
print(matchObj)
matchObj = re.match( r'(.*)(a)' , 'bcdefa' )
print(matchObj.group( 1 ))
print(matchObj.group( 2 ))
searchObj = re.search( r'a' , 'bcdefa' )
print(searchObj.group())

import re

phone = "2004-959-559 # Acesta este un numar de telefon"
num = re.sub( r'#.*$' , "" , phone)
print("Phone Num : " , num)
# Sterge orice din string mai putin numere
num = re.sub( r'\D' , "" , phone)
print("Phone Num : " , num)

import re

fileText = '<text top="52" left="20" width="383" height="15" font="0"><b>test</b></text>'
fileText = re.sub( "<b>(.*?)</b>" , r"\1" , fileText)
print (fileText)

print ( " \n\n FTP Module in Python \n\n " )
from ftplib import FTP
ftp = FTP( 'ftp.iinet.net.au' )
ftp.login( 'anonymous' , 'anonymouse' )
ftp.retrlines( 'LIST' )
#ftp.retrbinary('RETR welcome.msg', open('welcome.txt', 'wb').write)
ftp.quit()
print ( ' \n\n HTTP Module in Python - Requests \n\n ' )
