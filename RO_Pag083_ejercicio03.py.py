#RO_Pag083_ejercicio03

from math import*

print("introdueix un número de tres xifres:", end="")
n = int(input())

print("introdueix un número de tres xifres:", end="")
p = int(input())

d = n % 100
f = d // 10

s = p % 100
t = s //10

r = f + t
print("la suma de les dos xifres del mig és=", r)


