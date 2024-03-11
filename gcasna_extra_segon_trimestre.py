#gcasna_extra_segon_trimestre.py


print("files: ")
files = int(input())

print("columnes: ")
columnes = int(input())

#triangle
for fila in range (1, files):
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for i in range (1, fila +1):
        print(i, end="")
    for columne in range (1, fila):
        print(columne, end="")
    print("")
"""
n = 1
for fila in range (0, files):
    for columne in range (0, fila+1):
        print(n, end="")
        n = n +1
    print("")
"""