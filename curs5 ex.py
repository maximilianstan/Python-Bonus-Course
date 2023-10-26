# Captati ca argument numele unui fisier. Daca exista in directorul care la fel trebuei sa-l
# captati ca argument cititi-l. Pentru asta folositi doua clase una care citeste din director si
# vede daca fisierul este prezent alta care citeste fisierul. Fiecare din aceste clase trebuie
# sa folosesca metode si atribute.

import argparse

class WorkWithDirectoare ( object ):
    def __init__ ( self ,directory_name):
        self .directory_name = directory_name
    def ListeazaDirectorulSiCautaFisier( self ):
        import os
        return os.listdir( self .directory_name)

class WorkWithFile( object ):
    def __init__ ( self ,file_name):
        self .file_name = file_name
    def CitesteFisier( self ):
        with open ( self .file_name, mode = "rt" ) as file:
            print (file.readlines())
    def ExistaFisier( self ,lista_directoare):
        import os
        if self .file_name in lista_directoare:
            return True
        else :
            return False