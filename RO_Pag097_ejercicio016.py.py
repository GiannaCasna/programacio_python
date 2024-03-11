#RO_Pag097_ejercicio016.py

print("Introdueix el seu gènere: Dona (1) o Home (2)=")
g = int(input())

print("Introdueix la teva edat:")
edat = int(input())

if g == 1:
    p1 = (220 - edat) / 10
    print("Pulsacions= ", p1)
else:
    p2 = (210 - edat) / 10
    print("Pulsacions= ", p2)

