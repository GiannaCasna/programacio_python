#RO_Pag071_ejercicio5.py

from math import*

#apartat a) 

print("introdueix el valor de cada dipòsit menusal:")
p = float(input())

print("introdueix el valor de l'interes mansual:")
x = float(input())

print("nombre de dipòsits mensuals efectuats:")
n = float(input())

a = p * (((1 + x )**n - 1) / x)

print("valor acumulat=", a)

#apartat b)
"""
print("introdueix el valor de l'interes anual:")
x = float(input())

print("nombre de dipòsits anuals efectuats:")
n = float(input())

print("valor acumulat:")
a= float(input())

k = (((1 + x )**n - 1) / x)

p = a / k

dm = p / 12

print ("valor de cada dipòsit mensual=", dm)
"""

