#Exercici01_challenge.py

print("Introdueix el nombre d'usuaris:")
s = float(input())
n = 1

while n != s:
    print("Usuari", n, "introdueix la teva renda anual (€)")
    s = float(input())
    if s <= 10000:
        t = s * 0.05
        s = s - t
        print("Li correspon un impositiu del 5%: ", s)
    elif s > 10000 and s < 20000:
        m = s * 0.15
        s = s - m
        print("Li correspon un impositiu del 15%: ", s)
    elif s >= 20000 and s < 35000:
        v = s * 0.20
        s = s - v
        print("Li correspon un impositiu del 20%: ", s)
    elif s >= 35000 and s < 60000:
        r = s * 0.30
        s = r - s
        print("Li correspon un impositiu del 30%: ", s)
    elif s <= 60000:
        i = s * 0.45
        s = s - i
        print("Li correspon un impositiu del 45%: ", s)
    n = n + 1
