#RO_Pag096_ejercicio012.py

from math import*

print("nombre d'articles que ha comprat:")
articles = int(input())
print("preu per unitat:")
preu = float(input())

if articles <= 5:
    cost = articles * preu
    print("cost total = ", cost)    
elif articles > 5 and articles < 10:
    preu = preu / 1.05
    cost = articles * preu
    print("cost total = ", cost)
elif articles >= 10:
    preu = preu / 1.08
    cost = articles * preu
    print("cost total = ", cost)

    
    
    