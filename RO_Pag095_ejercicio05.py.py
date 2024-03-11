#RO_Pag095_ejercicio05.py

from math import*

print("introdueix un número:")
p = float(input())

r = p % 1

if r == 0:
    print("és un nombre enter")
    t = p % 7
    if t == 0:
        print("és un nombre múltiple de 7")
    else:
        print("no és múltiple de 7")

else:
    print("no és un nombre enter")
    