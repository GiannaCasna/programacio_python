#RO_Pag0121_ejemplo021_ranas_saltrandom.py

from random import*
x = 0
y = 0
i = 0

while not((x == 4 and y == 4) or (x == -4 and y == 4) or (x == 4 and y == -4) or (x == -4 and y == -4)):
    d = randint (1,4)
    i = i + 1
    if d == 1:
        x = x + 1
    else 


# if (abs(X) == 4
from random import*
pos_rana = 10
comptador = 0
while (pos_rana > 0 and pos_rana < 20):
    aleatori = random.randint(0,1)
    if aleatori == 0:
        salt = -1
    else:
        salt = 1
    pos_rana = pos_rana + salt
    cont = cont + 1;
    print("Posició de la granota:", pos_rana)
    