#RO_Pag0181_ejercicio021_triangulars.py

from math import*

"""
def triangular_while (n):
    base = n
    boles_totals = 0
    contador = 0
    while contador <= base:
        n = base - contador
        boles_totals = n + boles_totals
        contador = contador + 1    
    print(boles_totals)

n = int(input("número boles base: "))
triangular_while (n)

"""
"""
def triangular (n):
    base = n
    nb = 0
    for i in range (0, n+1):
        nb = nb + i
    print(nb)
      
n = (int(input("n= ")))
triangular (n)
"""
def triangular (n):
    base = n
    nb = 0
    for i in range (0, n+1):
        nb = nb + i
    return(nb)
      
n = (int(input("n= ")))
triangular (n)

def s_triangular():
    stotal = 0
    for i in range (0, n+1):
        stotal = stotal + triangular (i)
    print("total= ", stotal)
    
n = (int(input("n= ")))
s_triangular()

    