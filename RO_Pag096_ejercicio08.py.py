#RO_Pag096_ejercicio08

from math import*

print("nota 1 de l'estudiant 1:")
nota11= float(input())
print("nota 2 de l'estudiant 1:")
nota12= float(input())
print("nota 3 de l'estudiant 1:")
nota13= float(input())

print("nota 1 de l'estudiant 2:")
nota21= float(input())
print("nota 2 de l'estudiant 2:")
nota22= float(input())
print("nota 3 de l'estudiant 2:")
nota23= float(input())

if nota11 >= nota12 or nota11 >= nota13:
    if nota12 >= nota13:
        s = nota11 + nota12
    else:
        s = nota11 + nota13
else:
    s = nota12 + nota13

if nota21 >= nota22 or nota21 >= nota23:
    if nota22 >= nota23:
        t = nota21 + nota22
    else:
        t = nota21 + nota23
else:
    t = nota22 + nota23
    
if s > t:
    print("l'estudiant 1 té millor calificació")
elif s < t:
    print("l'estudiant 2 té millor calificació")
else:
    print("els estudinats 1 i 2 tenen la mateixa calificació")

    

    
    