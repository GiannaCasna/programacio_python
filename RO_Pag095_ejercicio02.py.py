#RO_Pag095_ejercicio02.py

from math import*

print("valor del radi del cilindre=")
radi = float(input())
print("valor de l'altura del cilindre=")
altura = float(input())

if altura > radi:
    volum = pow (radi, 2) * pi * altura
    print("El volum del cilindre és:", volum)

else:
    print("ERROR!")