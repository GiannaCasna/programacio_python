#RO_Pag096_ejercicio010.py

from math import*

print("introdueix el valor del costat1:")
c1 = float(input())

print("introdueix el valor del costat2:")
c2 = float(input())

print("introdueix el valor del costat3:")
c3 = float(input())

if c1 == c2 == c3:
    print("És un triangle equilater (té els tres costats iguals)")
elif c1 == c2 or c2 == c3 or c3 == c1:
        print("És un triangle isòsceles (té dos costat iguals i un diferent)")
elif c1 != c2 and c2 != c3:
    print("És un triangle escaler (té tots els costats diferents)")




