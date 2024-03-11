#RO_Pag0218_ejemplo_llista_eliminar.py

#Escriu un programa per eliminar els elements repetits d'una llista numèrica.

n = int(input("Quantitat de números (que té la llista): "))
v = []

for i in range (n):
    x =int(input("Introdueix el número = "))
    v.append(x)
    #v = [x] + v
print("Llista original: ", v)

u = []
for e in v:
    if e not in u:
        u.append(e)
print("Llista filtrada: ", u)
