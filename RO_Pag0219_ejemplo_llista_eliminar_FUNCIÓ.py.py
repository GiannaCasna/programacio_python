#RO_Pag0219_ejemplo_llista_FUNCIÓ.py

#Escriu una funció que rebi una llista i elimini els elements repetits.

def norep(v):
    u = []
    for e in v:
        if e not in u:
            u.append(e)
    return u

v = []
n = int(input("Quantitat de números: "))
for i in range (n):
    x = int(input("Introdueix el número = "))
    v.append(x)
    
#norep (v) /// no fa falta cridar la funció pq ja la cridem al print final i ja conté el valor final (return).
print(norep(v))
