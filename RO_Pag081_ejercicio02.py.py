#RO_Pag081_ejercicio02.py

from math import*

print("introdueix la capacitat en litres del cilindre:", end="")
litres=float(input())
print("introdueix l'altura en metres del cilindre:", end="")
altura=float(input())

capacitat = litres / 1000

d=sqrt((capacitat * 4)/(pi * altura))

print("diametre de la base=", d)


