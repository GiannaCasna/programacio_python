#RO_Pag0149_ejercicio035_entre_1/1000.py

from random import*

print("Introdueix un número entre 1 i 1000:")
a = int(input())

print("Introdueix un númemro entre 1 i 1000:")
b = int(input())

if a < 1 and a > 1000:
    print("ERROR!")
elif b < 1 and b > 1000:
    print("ERROR!")

for a in range (1, a+1):
    for b in range (1, b+1):
        x = 1000 - a
        y = 1000 - b
        suma = x + y
        resta = 1000 - suma
        producte1 = resta * 1000
        producte2 = x * y
        suma_final = producte1 + producte2
        