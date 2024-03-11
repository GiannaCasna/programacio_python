#RO_Pag096_ejercicio09.py

from math import*

print("nota 1 de l'estudiant:")
nota1= float(input())
print("nota 2 de l'estudiant:")
nota2= float(input())
print("nota 3 de l'estudiant:")
nota3= float(input())

if nota1 > nota2 and nota1 > nota3:
    max = nota1
    if nota2 < nota3:
        min = nota2
    else:
        min = nota3
elif nota2 > nota3 and nota2 > nota1:
    max = nota2
    if nota1 < nota3:
        min = nota1
    else:
        min = nota3
else:
    max = nota3
    if nota1 < nota2:
        min = nota1
    else:
        min = nota2
    
print("nota més alta:", max)
print("nota més baixa:", min)


