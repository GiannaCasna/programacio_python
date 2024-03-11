#RO_Pag095_ejercicio01.py

from math import*

print("Valor de l'altura del cilindre=")
altura = float(input())
print("Valor del radi del cilindre=")
radi = float(input())

if altura > radi:
    volum = pow (radi, 2) * pi * altura
    print("El volum del cilindre és:", volum)

else:
    area = 2 * pi * radi *(radi + altura)
    print("L'àrea és:", area)
    
