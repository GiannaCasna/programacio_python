#RO_Pag071_ejercicio2_area_triangle.py

from math import *

print("Introdueix el valor de la diagonal: ",end="")
d = float(input())

print("Introdueix el valor de l'angle: ",end="")
alfa = float(input())

alfa = alfa * (pi/180) #pas de graus a rad.

b= d * cos(alfa)
h = d * sin(alfa)

area = (b * h)/2
print("Area del triangle= ", area)