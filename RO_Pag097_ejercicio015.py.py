#RO_Pag097_ejercicio015.py

from math import*

print("Introdueix un número de tres xifres:")
n = int(input())

p = n // 100
dp = n % 100

d = dp // 10
c = dp % 10

m = (p * d) / 10
mo = (p*d) % 10

if mo < 9:
    print("El número és vàlid!")
    print("=", mo)
else:
    print("No és vàlid!")



    
    