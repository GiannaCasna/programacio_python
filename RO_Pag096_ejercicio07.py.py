#RO_Pag096_ejercicio07.py

from math import*

print("introdueix la temperatura=")
t = float(input())

print("si la temperatura és en ºF pulsa 1. Si la temperatura està en ºC pulsa 2")
p = int(input())

if p == 1:
    c = 5/9 * (t - 32)
    print("temperatura en ºC=", c)
elif p == 2:
    f = 32 + (9 * t / 5)
    print("temperatura en ºF=", f)

