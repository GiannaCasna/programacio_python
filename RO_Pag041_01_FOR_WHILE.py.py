#RO_Pag041_01.py

n = int(input("nombre de paquets= "))
max_pes = 0

for i in range (1, n + 1, 1):
    print ("pes del paquet", i, "en kg=")
    pes_del_paquet =float(input( ))
    if pes_del_paquet > max_pes:
        max_pes = pes_del_paquet

print("el pes del paquet més gran és: ", max_pes)

#resolusió amb While

n = 1
max_pes = 0
paquets = 3 (+ 1)
while n != paquets:
    print ("pes del paquet", n, "en kg=")
    pes_del_paquet = float(input())
    if pes_del_paquet > max_pes:
        max_pes = pes_del_paquet
    n = n + 1

print("el pes de paquet més gran és: ", max_pes)

