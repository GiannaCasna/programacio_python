#RO_Pag098_ejercicio023.py

from math import*

print("Insereix les tres notes que ha obtingut l'alumne:")
print("Nota número 1=")
n1 = float(input())
print("Nota número 2=")
n2 = float(input())
print("Nota número 3=")
n3 = float(input())

if n1 > n2 and n1 > n3:
    print("Ordre de les notes de més gran a més petita:", n1, n2, n3)
elif n2 > n3:
    print("Ordre de les notes de més petita a més gran:", n1, n3, n2)
if n2 > n3 and n2 > n1: 
    print("Ordre de les notes de més gran a més petita:", n2, n3, n1)
elif n3 > n1:
    print("Ordre de les notes de més petita a més gran:", n2, n1, n3)
if n3 > n1 and n3 > n2:
    print("Ordre de les notes de més gran a més petita:", n3, n1, n2)
elif n1 > n2:
    print("Ordre de les notes de més petita a més gran:", n3, n2, n1)
