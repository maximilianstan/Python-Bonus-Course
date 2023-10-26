# Creati un porgram care sa se vada diferenta intre variabilele unei instante si variabilele unei
# clase. Variabilele (atributele) unei clase se vad la fel in toate instantele.

class Dog:
    kind = 'caine' # class variable (class attribute) shared by all instances
    def __init__ ( self , name):
        self .name = name # instance attribute valabila doar pentru aceasta instanta
        self .kind = 5 # instance attribute valabila doar pentru aceasta instanta
d = Dog( 'Fido' )
e = Dog( 'Buddy' )
print (d.kind) #printeaza atributul instantei
print (Dog.kind) #printeaza atributul clasei daca nu mai declaram mai jos self.kind = 5 si primu print printa atributul clasei
print (e.kind) #printeaza atributul instantei
print (Dog.kind) #printeaza atributul clasei daca nu mai declaram mai jos self.kind = 5 si primu print printa atributul clasei
print (d.name) #printeaza atributul instantei
print (e.name) #printeaza atributul instantei