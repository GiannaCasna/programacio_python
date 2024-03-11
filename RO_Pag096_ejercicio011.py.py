#RO_Pag096_ejercicio011.py

from math import*

print("abscisa del primer punt:")
ap1 = float(input())
print("ordenada del primer punt:")
op1 = float(input())
print("abscisa del primer punt:")
ap2 = float(input())
print("ordenada del segon punt:")
op2 = float(input())

D1 = sqrt (pow(ap1, 2) + pow(op1, 2))
D2 = sqrt (pow(ap2, 2) + pow(op2, 2))

if D1 > D2:
    print("El punt 1 està més aprop del punt d'origen")
else:
    print("El punt 2 està més aprop del punt d'origen")