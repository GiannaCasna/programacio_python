#RO_Pag0111_ejemplo_promig.py

print("Calcula i mostra el promig d'un grup de dades ingressades des del teclat")

n = int(input("Quantitat de dades: "))
s = 0
for i in range (n):
    x = float(input("Introdueix la següent dada: "))
    s = s + x
p = s/n
print("El promig és: ", p)
