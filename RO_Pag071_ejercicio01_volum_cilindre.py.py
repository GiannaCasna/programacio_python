#RO_Pag071_ejercico1_volum_cilindre.py

from math import *

print("Introdueix el radi en m: ",end="")
radi = float(input())

print ("Introdueix l'altura en m: ",end="")
altura = float(input())

volum = (pi * pow(radi,2))*altura
print("Volum = ",volum, "m2")
