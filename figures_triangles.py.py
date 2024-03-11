#triangle.py

from math import*

print("files= ")
files = int(input())

print("columnes= ")
columnes = int(input())

"""
#Triangle normal (imparell)
for fila in range (0, files):
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for i in range (0, fila +1):
        print("*", end="")
    for columne in range (0, fila):
        print("*", end="")
    print("")
"""
"""
#Rombe normal
for fila in range (0, files):
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for i in range (0, fila +1):
        print("*", end="")        
    for columne in range (0, fila):
        print("*", end="")
    print("")
for fila in range (0, files - 1):
    for columne in range (0, fila + 1): 
        print(" ", end="")
    for i in range (0, columnes -fila-1):
        print("*", end="")
    for columne in range (0, columnes - fila - 2):
        print("*", end="")
    print("")
"""

#Rombe blanc, amb full d'* (rombe buit)
for fila in range (0, files):
    for columne in range (0, columnes - fila):
        print("*", end="")
    for columne in range (0, fila + 1): 
        print(" ", end="")
    for columne in range (0, fila):
        print(" ", end="")
    for i in range (0, columnes - (fila)):
        print("*", end="")        
    print("")

for fila in range (0, files):
    for columne in range (0, fila+1):
        print("*", end="")
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for columne in range (0, columnes - fila):
        print(" ", end="")
    for i in range (0, fila +1):
        print("*", end="")        
    print("")

