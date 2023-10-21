print ( "Exercitiul 1" )
a = [ 1 , 2 , 2 , 3 , 5 ]
a.append( 3 )
print (a)
del a[ 3 ]
print (a)
a.remove(a[ 2 ])
print (a)
a.pop( 2 )
print (a)
a = []
print (a)

print ( "Exercitiul 2" )
a = { 1 , 2 , 3 , 4 }
b = { 3 , 4 , 5 , 6 }
c = { 5 , 6 , 7 , 8 }
print (b.intersection(c))
print (c.intersection(b))
print (a.union(b))
print (b.union(a))
print (a.difference(b))
print (b.difference(a))

print ( "Exercitiul 3" )
t = { 'IBM' : 194 , 'AAPL' : 416 , 'GOOG' : 895 }
for a, b in t.items():
    print ( "{key} => {value}" .format( key =a, value =b))

keyss = list (t.keys())
valuess = list (t.values())

print (valuess[keyss.index( 'AAPL' )]) # functia index arata pozitia dand elementul intr-un array
print ( "Exercitii 4" )
def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"' .format( k =key, v = str (value))
    result += '>'
    return result
print (tag( 'img' , src = "monet.jpg" , alt = "Sunrise by Claude Monet" , border = 1 ))

print ( "Exercitiu optional 1" )
def min_lista(t):
    a = t[ 0 ]
    for i in t[ 1 :]:
        if i < a: a = i
    return a