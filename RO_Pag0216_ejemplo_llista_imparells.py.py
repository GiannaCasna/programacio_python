#RO_Pag0216_ejemplo_llista_imparells.py

#Programa per sumar valors imparells d'una llista.

n = int(input("Quantitat de números (que té la llista): "))
v = []
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
s = 0
for e in v:
    if e%2==1:
        s = s+e
print("Total = ", s)
        