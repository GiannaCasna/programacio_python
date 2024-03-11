#RO_Pag095_ejercicio03.py

from math import*

print("valor de la base o l'amplada del rectangle:")
base = float(input())
print("valor de l'altura del rectangle:")
altura = float(input())
print("valor de la profunditat del rectangle:")
fons = float(input())

diagonal1= sqrt (pow(altura, 2) + pow(base, 2))

diagonal2= sqrt (pow(altura, 2) + pow(fons, 2))

diagonal3= sqrt (pow(fons, 2) + pow(base, 2))

if diagonal1 == diagonal2 and diagonal2 == diagonal3:
    print("totes les diagonals són iguals, i tenen de valor:", diagonal1)
elif diagonal1 == diagonal2:
    if diagonal1 > diagonal3:
        print("les més grans són les diagonals 1 i 2=", diagonal1)
    else:
        print("la diagonal més gran és la 3=", diagonal3)
elif diagonal1 == diagonal3:
    if diagonal1 > diagonal2:
        print("les més grans són les diagonals 1 i 3", diagonal1)
    else:
        print("la diagonal més gran és la 2=", diagonal2)
elif diagonal2 == diagonal3:
    if diagonal2 > diagoonal1:
        print("les més grans són les diagonals 2 i 3=", diagonal2)
    else:
        print("la diagonal més gran és la 1=", diagonal1)
elif diagonal2 == diagonal1:
    if diagonal2 > diagonal3:
        print("les més grans són les diagonals 2 i 1=", diagonal2)
    else:
        print("la diagonal més gran és la 3=", diagonal3)
