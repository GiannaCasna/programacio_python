#RO_Pag0216_ejemplo_llista_imparells_FUNCIÓ.py

#Escriu una funció que sumi els elements imparells de la llista.

def suma_imparells(v):
    s = 0
    for e in v:
        if e%2==1:
            s = s + e
    return (s)

n = int(input("Quantitat de números (que té la llista) ="))
v = []
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
print(suma_imparells(v))

        
            