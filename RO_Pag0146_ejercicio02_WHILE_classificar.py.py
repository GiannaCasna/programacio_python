#RO_Pag0146_ejercicio02_WHILE_classificar.py

#while
print("Introdueix el nombre d'objectes:")
objectes = int(input()) + 1
n = 1

while n != objectes:
    print("pes de l'objecte", n, "en Kg = ")
    pes_objecte = int(input())
    if pes_objecte < 10:
        a = n
    elif pes_objecte > 10 and pes_objecte < 20:
        b = n
    elif pes_objecte > 20:
        c = n
    n = n + 1

print("Nombre de pequets que tenen un pes menor a 10 kg:", a)
print("Nombre de pequets que tenen un pes entre 10 kg i 20 kg:", b)
print("Nombre de pequets que tenen un pes superior a 20 kg:", c)

        
    
