#RO_Pag0150_ejercicio036.py

from math import*
print("Intorudeix un valor a n =")
n = int(input())

print("Introdueix un valor a m =")
m = int(input())
i = 1
j = 1

for i in range (1, n):
    for j in range (1, m+1):
        suma = (pow(i,2) + pow(j, 2) + i*j)
print("Resultat de suma =", suma)

    
