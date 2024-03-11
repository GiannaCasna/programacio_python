#RO_Pag0180_ejercicio01_divisors.py

from math import*

def conteo(n):
    counter = 0
    for i in range (1, n+1):
        if n% i == 0:
            counter = counter + 1
    return (counter)
divisorss = 0             
maxim = 0
for n in range (1,101):
    counter = conteo(n)
    print("número de divisors de ", n,"=", counter)
    if counter > divisorss:
        divisorss = counter
        maxim = n
print("El número amb més divisors entre 1 i 100 és: ", maxim)
print("El número de divisors és = ", divisorss)

    
