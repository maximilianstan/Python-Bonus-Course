x = 7
y = 2
print (x+y)
print (x-y)
print (x*y)
print (x/y)
print (x%y)
print (x** 2 )
print (x // y)
c = x + y
print (c)
print ( "Operatori de initializare in Python" )
a = 3
c = c + a
print (c)
c -= a
print (c)
c *= a
print (c)
c /= a
print (c)
print ( "Round in Python" )
print ( round ( 3.3 ))
print ( round ( 3.6 ))
print ( round ( 3.5 ))
print ( "Ceil & Floor in Python" )
import math
print (math.ceil( 3.3 ))
print (math.ceil( 3.6 ))
print (math.floor( 3.3 ))
print (math.floor( 3.6 ))
print ( "Printarea pe linie noua in Python" )
m = "This string \n spans multiple \n line"
print (m)
m = """This is
a multiline string"""
print (m)
print ( "Printarea cu tab in Python" )
m = "test1 \t tes2"
print (m)
m = "test1 \t\t tes2"
print (m)
m = "test \' "
print (m)
m = "test \" "
print (m)
m = 'test "'
print (m)
m = "test '"
print (m)
print ( "Asa se printeaza backslash in Python \\ " )
print ( 'Asa nu se printeaza backslash in Python \ ' )
print ( "Asa nu se printeaza \ backslash in Python \ " )

#https://docs.python.org/2/reference/lexical_analysis.html#string-literals - se poate vedea ca daca lasam un spatiu nu da
#eroare deoarece \ nu e cunoscut ca escape ca sa fie escape dupa el trebuie sa urmeze ce e in link astfel e literar

m= r'C:\Users\Merlin\Documents\Spells'
print (m)
print ( r'\\' )
print ( r'c:\test' + ' \\ ' )
print ( r'test1\n test2' )
print ( 'test1 \n test2' )
print ( "Operatori decizionali in Python" )
g = 20
print (g== 20 )
print (g == 13 )
print (g != 20 )
print (g != 13 )
t = "telacad"
print (t == "telacad" )
print ( "Operatori logici in Python" )
print (( 9 > 7 ) and ( 2 < 4 ))
print (( 8 == 8 ) or ( 6 != 6 ))
print ( not ( 3 <= 1 ))
print ( "If in Python" )
if True :
    print ( "expresia este adevarata" )
if False :
    print ("expresia nu este evaluata" )
if bool ( "telacad" ):
    print ( "expresia este evaluata" )
if "telacad" :
    print ( "expresia este evaluata" )
    print ( "If elif else in Python" )
inaltimea = 60
if inaltimea > 50 :
    print ( "Inaltimea este mai mare ca 50" )
elif inaltimea < 20 :
    print ( "Inaltimea este mai mica decat 20" )
elif 30 >= inaltimea > 20 :
    print ( "Inaltimea este intre 20 si 30" )
else :
    print ( "Inaltimea este intre 30 si 50" )
    print ( "While in Python" )

c = 5
while c:
    print (c)
c -= 1
print ( "Break in Python" )
c = 5
while True :
    print (c)
    if c == 3 :
        break
c -= 1
print ( "Aici am ajuns iesind din bucla cu " )
print ( "Continue in Python" )
d = 10
while d:
    d = d - 1
    if d == 5 :
        break
print ( "Acest text nu va fi printat" )
print ( "For in Python" )
for i in range ( 5 ):
    print (i)
words = [ 'cat' , 'window' , 'defenestrate' ]
for w in words:
    print (w, len (w))