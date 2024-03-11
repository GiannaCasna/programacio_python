#RO_Pag0100_ejemplo_IF/ELSE_random.py

"""
Números d'un dau.
Escriu un programa que generi un número aleatori d'un dau.
Si surt el número 6 mostra el missatge: Afortunat.
En cas contrari, mostra el número obtingut i el missatge: No hi ha hagut sort.
"""
from random import*

n = randint (1,6)
if n == 6:
    print("Afortunat!!")
else:
    print("número:", n)
    print("No hi ha hagut sort")
    