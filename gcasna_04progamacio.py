#gcasna_04.py

from math import*

def equacio_2ngrau(a,b,c):
    tt = b**2-(4*a*c)
    t = sqrt(tt)
    q = -b + t
    s = -b - t
    if t < 0:
        print("Les solucions són imaginàries")
    else:
        print("Solució 1 = ", q)
        print("Solució 2 = ", s)

print("Introdueix els següents valors per resoldre l'equació de segon grau.")
a = int(input("Valor de a= "))
b = int(input("Valor de b= "))
c = int(input("Valor de c= "))

equacio_2ngrau(a,b,c)
