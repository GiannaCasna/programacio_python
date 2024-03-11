#gcasna_3.py

from math import*

def gelat (d):
    c = 2,25€
    r = d - c
    print("canvi = ", r)

def pastis (d):
    c = 1,75€
    r = d - c
    print("canvi = ", r)
    
def galetes (d):
    c = 2,50€€
    r = d - c
    print("canvi = ", r)

def bombons (d):
    c = 3€
    r = d - c
    print("canvi = ", r)

sortida = False
while not sortida:
    print("Productes disponibles:")
    print("1. Gelat d'avellana = 2,25€")
    print("2. Patstis d'ametlla = 1,75€")
    print("3. Galetes de xocolata blanca = 2,50€")
    print("4. Bombons de caramel = 3€")
opcio = int(input("Escull el número del producte que vulguis:"))

if opcio == 1:
    d = float(int("diners = "))
    gelat

elif opcio == 2:
    d = float(int("diners = "))
    pastis

elif opcio == 3:
    d = float(int("diners = "))
    galetes

elif opcio == 4:
    d = float(int("diners = "))
    bombons

    
    
    