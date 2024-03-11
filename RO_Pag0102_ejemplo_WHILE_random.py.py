#RO_Pag0100_ejemplo_WHILE+random.py

"Simular el llençament d'un dau fins que surti el número 3"
from random import*

s = 0

while s != 3:
    s = randint (1,6)
    print(s)

    