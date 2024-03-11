#RO_Pag0146_ejercicio01_WHILE.py

#WHILE
print("Introdueix el nombre de pequets:")
paquets = int(input()) + 1
max_pes = 0
n = 1
while n != paquets:
    print("pes del paquet", n, "en Kg:")
    pes_del_paquet = float(input())
    if pes_del_paquet > max_pes:
        max_pes = pes_del_paquet
    n = n + 1

print("El pes del paquet més gran és :", max_pes, "Kg")
    
    
    
