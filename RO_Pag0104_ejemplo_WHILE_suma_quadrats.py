#RO_Pag0104_ejemplo_WHILE_suma_quadrats.py

"SUMA de quadrats"
n = int(input("Introdueix el valor final: "))
s = 0
i = 1
while i <= n:
    c = i **2
    s = s+c
    i = i + 1
print("La suma és= ", s)

