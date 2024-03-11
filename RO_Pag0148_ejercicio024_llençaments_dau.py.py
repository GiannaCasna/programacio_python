#RO_Pag0148_exercici24.py

from random import*
print("Introdueix el nombre de llençaments del dau:")
llen = int(input())
n = 1
c = 0

while n <= llen:
    p = randint (1,6)
    if p == 6:
        c = c + 5
    elif p == 1:
        c = c + 1
    else:
        c = c - 2
    print("llençament", n,"=", p, end="")
    print(" dolars", c)
    n = n + 1
    
print("Quantitat de dolars finals:", c)
    
        