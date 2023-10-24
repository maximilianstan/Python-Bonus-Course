x = 500
y = x
print ( id (x))
print ( id (y))
y = 200
print (x)
print (y)
print ( id (x))
print ( id (y))
x = 500
print ( id (x)) # in Pychamr asta si cu printul de mai jos dau acelasi rezultat din cauza interpretului de fapt sunt adrese
# de memorie diferite
x = 500
print ( id (x)) # in Pychamr asta si cu printul de mai sus dau acelasi rezultat din cauza interpretului de fapt sunt adrese
# de memorie diferite
t = 5
print ( str (t) + '->' + str ( id (t)))
t = t + 2
print ( str (t) + '->' + str ( id (t)))
print ( isinstance ( 500 , object ))
print ( isinstance ( "test" , object ))
x = 500
print ( isinstance (x, object ))
r = [ 2 , 4 , 6 ]
print (r)
s = r
print (s)
s[ 1 ] = 17
print (s)
r[ 0 ] = 3
print (r)
print (s)
print (s is r)
print ( "Egalitatea ca valoare vs identiatea" )
p = [ 4 , 7 , 11 ] # aici se poate vedea cum avem egalitate dar nu identiate si modificare lui p sau q nu se reflecta la
# ambele ci doar la cel modificat
q = [ 4 , 7 , 11 ]
print (p == q)
print (p is q)
q = p
print (p is q)
p[ 1 ] = 3
print (p) #printul asta cu cel de mai jos din cauza pycharm dau ca si cum sunt modificate amandaou dar in terminal se poate
# vedea clar ca doar una e modificata
print (q)
print ( "Argument parsing from object perspective" )

def modify(y):
    y = y + 3
    print (y)

t = 2
modify(t)
print (t)
def modifylistorint(y,z):
    y = y + z
    print ( "modifylistorint " + str (y))

v = 3
h = 2
modifylistorint(v,h)
v = [ 3 , 2 ]
h = [ 1 ]
modifylistorint(v,h)
x = [ 1 , 2 , 3 ]
def modifylist(a):
    a.append( 39 )
    print ( "a=" ,a)
modifylist(x)
print (x)
def f(d):
    return d
c = [ 6 , 10 , 16 ]
e = f(c)
print (c is e)
o = 3
m = f(o)
print (o is m)
print ( "Dynamic Typed" )
def add(a, b):
    return a + b
print (add( 5 , 7 ))
print (add( 3.1 , 2.4 ))
print (add( "news" , "paper" ))
print (add([ 1 , 6 ], [ 21 , 106 ]))
#print(add("The answer is", 42)) - asta da eroare deoarece e strong nu poate aduna un string cu un integer
print ( "Scope and Namespace in Python" )
count = 0
def show_count():
    print ( "count = " , count)
def set_count(c):
    count = c
show_count() # nu gaseste in interior si se uita in outer namespace
set_count( 5 ) # asta modifica doar local
show_count()
print ( "Scope and Namespace in Python and Global" )
count = 0
def show_count():
    print ( "count = " , count)

def set_count(c):
    global count # acum asta face rebind in namespace-ul principal (adica o face globala pe variabila)
    count = c
show_count() # nu gaseste in interior si se uita in outer namespace
set_count( 5 ) # acum asta o sa modifice globla
show_count()
print ( "Everything is an object in Python and testing with type" )

class TelecomAcademy:
    pass # nu fa nimic merge mai departe in program (ca la poker)
TelecomAcademy()
print ( "Clase in Python" )
print ( type ( 5 ))
print ( type ( "python" ))
print ( type ([ 1 , 2 , 3 ]))
class Dog:
    kind = 'caine' # class variable (class attribute) shared by all instances
def __init__ ( self , name):
    self .name = name # instance attribute valabila doar pentru aceasta instanta
    self .kind = 5 # instance attribute valabila doar pentru aceasta instanta
d = Dog("Fido")
e = Dog("Buddy")

print (d.kind) #printeaza atributul instantei
print (Dog.kind) #printeaza atributul clasei daca nu mai declaram mai jos self.kind = 5 si primu print printa atributul clasei
print (e.kind) #printeaza atributul instantei
print (Dog.kind) #printeaza atributul clasei daca nu mai declaram mai jos self.kind = 5 si primu print printa atributul clasei
print (d.name) #printeaza atributul instantei
print (e.name) #printeaza atributul instantei
print ( "Mostenirea in Python" )
class ClasaDeBaza:
    def __init__ ( self ):
        print ( 'ClasaDeBaza init' )
    def f( self ):
        print ( 'ClasaDeBaza.f()' )
class Sub(ClasaDeBaza):
    def __init__ ( self ):
        print ( 'sub init' )
    def f( selfs ):
        print ( 'Sub.f()' )
s = Sub()

print ( "Mostenirea in Python cu super" )
class ClasaDeBaza:
    def __init__ ( self ):
        print ( 'ClasaDeBaza initializer' )
    def f( self ):
        print ( 'ClasaDeBaza.f()' )
class Sub(ClasaDeBaza):
    def __init__ ( self ):
        super (). __init__ ()
    print ( 'sub initializer' )
    def f( self ):
        super ().f()
    print ( 'Sub.f()' )

s = Sub()
s.f()