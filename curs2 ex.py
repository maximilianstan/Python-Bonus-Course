user_input = ""
while user_input != "telacad":
    user_input = input("Introduceti string-ul telacad: " )
print("Sfarsitul programului")

#Telacad_sedinta2_2.py

while True :
    n = input ( "Introduceti un numar: " )
    if int (n) > 2 :
        break
a = 0
for i in range ( int (n)+ 1 ):
    a = a + i
print (a)

#Telacad_sedinta2_3.py

secventa = [ "telacad" , "peste 10 ani vechime" , "predare" , "cursuri online" ]
propozitie = ""
for w in secventa :
    propozitie = propozitie + w + " "
print (propozitie)

#Telacad_sedinta2_4.py

x = 2 + 3j
# x = 2.3
# x = 7
if isinstance (x, int ):
    print (x+ 3 )
elif isinstance (x, float ):
    print (x/ 2 )
elif isinstance (x, complex ):
    print (x.imag)
    print (x.real)
    print ( abs (x))
else :
    print ( "nimic nu se potriveste" )