#RO_Pag083_ejercicio04

from math import*

print("introdueix un número de tres xifres:")
n = int(input())

c = n // 100
du = n % 100

d = du // 10
u = du % 10

print("xifra girada =", u, d, c)