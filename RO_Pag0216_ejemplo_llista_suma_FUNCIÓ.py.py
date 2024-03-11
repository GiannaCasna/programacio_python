#RO_Pag0216_ejemplo_llista_suma_FUNCIÓ.py

#Escriu una funció que sumi tots els elements de la llista.

def suma(v):
    s = 0
    for e in v:
        s = s + e
    return s

n = int(input("Quantitat de números (que té la llista): "))
v = []
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
    
print (suma(v))
        
    