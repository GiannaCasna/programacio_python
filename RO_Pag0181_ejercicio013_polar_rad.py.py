#RO_Pag0181_ejercicio013_polar_rad.py

from math import*

def polar(x, y):
    r = sqrt(x**2 + y**2)
    t = atan (y/x)
    t = (t*180) / pi
    print("Coordenades polars: r = ", r, "t = ", t)

def cartesiana(r, t):
    t = t * pi / 180
    x = r * cos(t)
    y = r * sin(t)
    print("Coordenades cartesianas: x = ", x, "y = ", y)

sortida = False
while not sortida:
    print("Escull una de les tres opcions següents:")
    print("1. Convertir a polars")
    print("2. Convertir a cartesians")
    print("3. Sortir")
    print("Escriu: 1, 2 o 3 =")
opcio = int(input("Escull una opció:"))

if opcio == 1:
    x = int(input("valor de x = "))
    y = int(input("valor de y = "))
    polar(x, y)
elif opcio == 2:
    r = int(input("valor de r = "))
    t = int(input("valor de t = "))
    cartesiana(r, t)
elif opcio == 3:
    print("SALIR!!")
    sortida = True
    
    