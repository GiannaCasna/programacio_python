#RO_Pag098_ejercicio021.py

from math import*

print("Introdueix tres números d'una metriu quadrada de tamany 2:")
print("número 1 = ")
n1 = int(input())
print("número 2 = ")
n2 = int(input())
print("número 3 = ")
n3 = int(input())
n4 = 0

if abs (n1 ** 2) - abs (n2 ** 2) == 0:
    n4 = n3 * (-1)
print("el valor del número 4 de la meriu és: ", n4)
