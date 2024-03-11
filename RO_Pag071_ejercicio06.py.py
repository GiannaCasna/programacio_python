#RO_Pag071_ejercicio6.py

from math import*

print("introdueix dos nombres enters entre 1 i 1000:")
x = int(input())
y = int(input())
#rrp = resultat resta amb el primer nombre
#rrs = resultat resta amb el segon nombre
#srr = suma dels resultat de la resta
#rs = resta de 1000 el resultat de la suma
#m = mutiplicar el resultat de la suma per 1000
#mri = mutiplicar el resultat de les restes inicials
#sur = suma dels dos últims resultats

rrp = 1000 - x
rrs = 1000 - y
srr = rrp + rrs
rs = 1000 - srr
m = rs * 1000
mri = rrp * rrs
sur = m + mri

print("resultat final=",sur,)
print( x * y) #comprovació de que és correcte


