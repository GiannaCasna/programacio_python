#RO_Pag0150_ejercicio037_número_d'or.py

from math import*

def numero_aureo (n):
    a = 0
    b = 1
    while a <= n:
        a = b + sqrt((pow(b,2)) - 4*(pow(b,2)))
        
        z = a//1
        if a / z == 1:
            print("pareja de aureo", a, "y", b)
        b = b + 1
        a = a//1

n = int(input("n =", ))
numero_aureo (n)
