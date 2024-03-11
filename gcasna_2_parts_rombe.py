#gcasna_2.py

from math import*

# *****
# ****
# ***
# **
# *

"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files):
    for columne in range (0, columnes - fila):
        print("*", end="")
    print("")
"""
# *
# **
# ***
# ****
# *****
"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files):
    for columne in range (0, fila+1):
        print("*", end="")
    print("")
"""
#      *
#     **
#    ***
#   ****
#  *****
"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files):
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for i in range (0, fila +1):
        print("*", end="")        
    print("")
"""
# *****
#  ****
#   ***
#    **
#     *

"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files):
    for columne in range (0, fila + 1): 
        print(" ", end="")
    for i in range (0, columnes - (fila)):
        print("*", end="")        
    print("")
"""
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *
"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files):
    for columne in range (0, columnes - (1 + fila)): 
        print(" ", end="")
    for i in range (0, fila +1):
        print("*", end="")        
    print("")
for fila in range (0, files):
    for columne in range (0, fila): 
        print(" ", end="")
    for i in range (0, files - fila):
        print("*", end="")        
    print("")
"""
print("files= ")
files = int(input())
print("columnes= ")
columnes = int(input())

for fila in range (0, files - 1):
    for columne in range (0, fila+1):
        print("*", end="")
    print("")
for fila in range (0, files):
    for columne in range (0, columnes - fila):
        print("*", end="")
    print("")

    
    
        