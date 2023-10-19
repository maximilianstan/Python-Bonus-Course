s = 'Academie'
print ( len (s))
print (s[ 0 ])
print (s[ 1 ])
print ( "Ultimul element din string: " + str (s[- 1 ]))
print ( "Penultimul element din satring: " + str (s[- 2 ]))
print ( " \n " )
print ( "Captam anumite secvente din string" )
print (s[ 1 : 3 ])
print (s[ 1 :])
print (s[ 0 : 3 ])
print (s[: 3 ])
print (s[:- 1 ])
print (s[:])
print (s * 3 )
print (s.upper())
# s[0] = "a" - nu merge deoarece stringurile sunt imutable (nu se pot modifica)
print ( "Aici se va crea alt obiect in memorie si se va schimba referinta" )
s = 'z' + s[ 1 :]
print (s)
print ( "Split in Python" )
line = 'aaa, bbb, ccc'
print (line.split( ',' ))
line = 'aaa, bbb, cc \n '
print (line.rstrip())
print ( "%s, eggs, and %s" % ( 'spam' , 'SPAM!' ))
L = [ 2.35 , 'spam' , 354 ]
print ( len (L))
print (L[ 0 ] + 1 )
print (L[:- 1 ])
print (L + [ 4 , 5 , 6 ])
print (L)
L.append( 'NI' )
print (L)
L = [ 2.35 , 'spam' , 354 ]
L.pop( 2 )
L.append( 354 )
del L[ 2 ]
L.append( 354 )
L.remove( 354 )
L.append( 354 )
print (L)
M = [ 'bb' , 'aa' , 'cc' ]
M.sort()
print (M)
M.reverse()
print (M)
L = [ '2.35' , 'spam' , '354' ]
L.sort()
print (L)
# L[99] - da eroare daca elementul din listaa nu exista - putem adauga oricate de multe elemente dar cand extragem trebuie sa fim siguri ca exista
lista = [ 1 , 2 , 3 ]
lista[ 2 ] = 5
print (lista)
del lista[ 2 ]
lista.append( 3 )
print (lista)
print ( max (lista))
print ( min (lista))
for x in lista: print (x)
t = list ( "test" )
print (t)
for i in "test" :
    print (i)
print ( "Matrici in Python" )
M = [[ 1 , 2 , 3 ], [ 4 , 5 , 6 ], [ 7 , 8 , 9 ]]
print (M[ 1 ])
print (M[ 1 ][ 2 ])
print ( "Tuples in Python - la fel ca lista doar ca e immutable si are paranteze rotunde" )
t = ( "Bucuresti" , 4.953 , 3 )
print (t)
print (t[ 0 ])
print (t[ 2 ])
# t[0] = "B"
print ( len (t))
print ( "La fel ca la lista putem itera in tuples" )
for item in t: print (item)
print (t + ( 33.6 , 44 , 5 ))
print (t * 3 )
h = ( 391 )
print ( type (h))
k = ( 391 ,)
print ( type (k))
print ( "Deoarece tuplul este immutable nu putem vorbi de a scoate elemente sau modifica elemente" )
k = ( 3 , 5 , 17 , 257 , 65537 )

#k.remove(3) #-aceasta instructiune ar da eroare
#del k[3] #-aceasta instructiune ar da eroare
#k.discard(3) #-aceasta instrunctiune ar da eroare

print ( "Set in Python" )
p = { 6 , 28 , 496 , 8128 , 33550336 } # asa se intializeaza un set cu valori nu empty
print (p)
print ( type (p))
d = {} # nu se initializeaza asa empty set (aici de fapt e un dictionar)
print ( type (d))
e = set () # asa se initializeaza empty set
print ( type (e))
s = set ([ 2 , 4 , 16 , 64 , 4096 , 65534 ])
print (s)
q = { 2 , 9 , 6 , 4 }
print ( 3 in q)
print ( 3 not in q)
k = { 81 , 108 }
k.add( 54 )
k.update([ 37 , 128 , 97 ])
k.remove( 97 ) # se observa ca pentru a face remove avem nevoie sa dam ca argument elementul din tuplu
k.discard( 97 ) # se observa ca face acelasi lucru ca remove dar nu da eroare in caz ca elementul exista
k.pop() #fara argumente scoate primul argument din set
print (k)
k.remove( 37 )
print (k)
a = { 1 , 2 , 3 }
b = { 2 , 3 , 4 , 5 }
print (a.union(b))
print (a.intersection(b))
print (a.difference(b))
print ( "Dictionare in Python key immutable valori mutable" )
names_and_ages = [( 'Alice' , 32 ), ( 'Bob' , 48 ), ( 'Charlie' , 28 ), ( 'Daniel' , 33 )]
d = dict (names_and_ages)
print (d)
stocks = { 'GOOG' : 891 , 'AAPL' : 416 , 'IBM' : 194 }
stocks.update({ 'GOOG' : 894 , 'YHOO' : 25 })
print (stocks)
print (stocks[ 'GOOG' ])
stocks[ 'GOOG' ] = 895
print (stocks)
print ( "In dictionare print se face peste key sau peste valori" )
print ( "Printarea de valori" )
for i in stocks.values():
    print (i)
print ( "Printarea de keys" )
for i in stocks.keys():
    print (i)
for key, value in stocks.items():
    print ( "{key} => {value}" .format( key =key, value =value))
    print ( "GOOG" in stocks)
    print ( "GOOGLE" in stocks)
    print ( "GOOGL" not in stocks)
    del stocks[ 'YHOO' ]
    print ( "remove, discard sau pop or sa dea eroare nu sunt specifice dictionarelor in Python" )
    print (stocks)
    print ( "Functii in Python" )
def square(x):
    return x * x
print (square( 5 ))
def even_or_odd(n):
    if n % 2 == 0 :
        return "even"
    return "odd"

print (even_or_odd( 4 ))
print (even_or_odd( 5 ))

def banner(message, border= '-' ):
    line = border * len (message)
print (line)
print (line)
banner( "Norwegia Blue" )
