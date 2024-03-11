#RO_Pag081_exercicio01_cilindre_area_volum

from math import*

print("introdueix el radi del cilindre:", end="")
radi = float(input())

print("introdueix l'altura del cilindre:", end="")
altura = float(input())

area = 2 * ( pi * pow(radi, 2)) + 2 * pi * radi * altura

volum = pi * pow(radi, 2) * altura

print("area total=", area)
print("volum total=", volum)
