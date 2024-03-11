#gcasna_1.py

from math import*

def funcio01 (a):
    a = a * pi / 180
    for i in range (0, 360+1):
        y = 4 + sin(a)
        print("y = ", y)

def funcio02 (a):
    a = a * pi / 180
    y = 4 + 230 * sin(a)
    print("y = ", y)
    
a = int(input("valor d'alpha = "))
i = 0
#els intervals de l'angle 45º, des de 0 fins a 360 són: 0, 45, 90, 135, 180, 225, 270, 315, 360
for i in range (45, 90, 135, 180, 225, 270, 315, 360):
print("per a funció n.01: ")
    y = funcio01

    print(y , i)