#RO_Pag0216_ejemplo_llista_parells_FUNCIÓ.py

#Escriu una funció que sumi tots els números parells de la llista.

def suma_parells(v):
    s = 0
    for e in v:
        if e%2==0:
            s = s + e
    return(s)

n = int(input("Quantitat de números (que té la llista) ="))
v = []
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
print(suma_parells(v))
    