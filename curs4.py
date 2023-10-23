# scrierea_in_fisier.py

f = open("testwrite.txt", mode = "wt", encoding = "utf-8")
print(f.write("Test linia 1, "))
f .write("continuare linia 1 \n ")
f .write("Sfarsit de fisier care e linia 2")
f .close()

# citirea_din_fisier.py

g = open ("testwrite.txt", mode = "rt", encoding = "utf-8")
print (g.read( 14 ))
print (g.read())
print (g.seek( 0 ))
print (g.readline())
print (g.readline())
print (g.readline())
print (g.seek( 0 ))
print (g.readline())
print (g.seek( 0 ))
print (g.readlines())
g.close()

# adaugarea_de_text_in_existing_file.py

h = open ("testwrite.txt", mode = "at", encoding = "utf-8")
h. writelines (["\n Alt text la fisierul deja existent \n", "A doua linie la fisierul deja existent \n "])
h.close()

# context_manager_read_file.py

with open ("testwrite.txt", encoding = "utf-8") as file:
    print (file.readlines())

# context_manager_write_file.py

with open("testwritetest.txt", encoding="utf-8") as file:
    file .write("Linia 1 \n")
    file .write("Linia 2")

# context_manager_write_file.py

with open ("testwritetest.txt", mode = "wt" , encoding = "utf-8") as file:
    file.write("Linia 1\n")
    file.write("Linia 2\n")
    file.write("Linia 3\n")

#context_manager_append_to_file.py

with open ("testwrite.txt", mode = "at", encoding = "utf-8") as h:
    h.writelines([" \n Linie 4 \n ", "linie 5 \n "])

# testwrite.txt

# Test linia 1, continuare linia 1
# Sfarsit de fisier care e linia 2
# Alt text la fisierul deja existent
# A doua linie la fisierul deja existent

# Words.py
def fetch_words():
    with open ("t.txt") as file:
        file_words = []
        for line in file:
            line_words = line.split()
            for word in line_words:
                file_words.append(word)

    for word in file_words:
        print (word)

if __name__ == "__main__" :
    fetch_words()

# Atentie cand rulam programul de mai sus din command line sau pycharm ne de __mai__ altfel daca folosim import ne da numele programului in acest caz words.py

# Lucrul cu argumente (argparse)

import argparse

parser = argparse.ArgumentParser(description = "TEST")

parser.add_argument("square" , type = int ,
        help = "afiseaza patratul unui numar")
parser.add_argument("-v", "--verbose", action = "store_true",
        help = "creste verbosity la afisare")
parser.add_argument("-a", action = "append", dest = "collection",
        default =[],
        help = "Adauga valori la lista",
        )

args = parser.parse_args()
answer = args.square** 2
a = args.collection
for i in a:
    print (i)
    print (a)
if args.verbose:
    print ("patratul lui {} egal cu {}" .format(args.square, answer))
else :
    print (answer)

# Rulat cu argumentii de mai jos da urmatorul output

#/usr/bin/python3.5 /home/pandelegeorge/projects/telacad/sedinta5/argparse_test.py 2 -a 1 -a 2 -a 5 -v
#1
#2
#5
#['1', '2', '5']
#patratul lui 2 egal cu 4
#Process finished with exit code 0

#Exceptii in Python

#Program1.py

x,y = (5, 0)
try :
    z = y/x
except :
    z = x/y
finally :
    print ("Final de program")

print (z)

# Program2.py

y, x = (5, 0)
try :
    z = y/ x
except :
    z = x /y
finally :
    print ("Final de program")
print (z)