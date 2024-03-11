#RO_Pag0110_ejemplo_suma_quadrats.py

print("Necessitem sumar els quadrats dels primers n números naturals")

n = int(input("Introdueix el valor final: "))
s = 0
for i in range (1, n+1):
    c = i **2
    s = s + c
print("La suma és: ", s)
