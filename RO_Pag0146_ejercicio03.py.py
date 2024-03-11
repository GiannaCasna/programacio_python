#RO_Pag0146_ex03.py

from math import*

print("Introdueix el valor a superar per la sèrie:")
x = int(input())
base = 1
exponent = 1
suma = pow(base, exponent)
i = 1

while suma < x:
    base = base + 1
    exponent = exponent + 1
    suma = pow(2,i) + suma
    print(pow(2,i), "", suma)
    x = x + 1