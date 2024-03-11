#RO_Pag0216_ejemplo_llista_parells.py

#Programa per sumar valors parells d'una llista.

print("Quantitat de números (que té la llista):")
n = int(input())

v = []
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
    #v = [x] + v /// això serveix per afegir un número a la llista.

s = 0
for e in v:
    if e%2== 0:
        s = s + e

print("Total:", s)
