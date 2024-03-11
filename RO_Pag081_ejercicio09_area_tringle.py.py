#RO_Pag081_ejercicio09_area_triangle

from math import*

print("valor de a=", end="")
a = float(input())

print("valor de b=", end="")
b = float(input())

print("valor de c=", end="")
c = float(input())

print("valor de d=", end="")
d = float(input())

x=sqrt((c-a)**2 + (d-b)**2)

y=sqrt((0-a)**2 + (0-b)**2)

z=sqrt((c-0)**2 + (d-0)**2)

t= (x + y + z)/2

R= sqrt(t*(t-x)*(t-y)*(t-z))

print("area del triangle=", R)
