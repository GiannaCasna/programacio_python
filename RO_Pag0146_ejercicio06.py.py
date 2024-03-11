#RO_Pag0146_ejercicio06

print("Introudeix el nombre de les persones a votar:")
v = int(input())

a = 0
b = 0
c = 0
v_blanc = 0
nul = 0

n = 0

while n < v:
    vot = int(input("Introdueix el vot:"))
    
    if vot == 1:
        a = a + 1
    elif vot == 2:
        b = b + 1
    elif vot == 3:
        c = c + 1
    elif vot == 0:
        v_blanc = v_blanc + 1
    else:
        nul = nul + 1
    n = n + 1

print("Total de vots del primer candidat =", a)
print("Total de vots del segon candidat =", b)
print("Total de vots del tercer candidat =", c)
print("Quantitat de vots en blanc =", v_blanc)
print("Quantitat de vots nuls =", nul)