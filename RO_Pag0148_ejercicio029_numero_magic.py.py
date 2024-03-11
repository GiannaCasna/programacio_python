#RO_Pag0148_ejercicio029_nombre_magic.py

dia = 30
mes = 12
anY = 2007

suma = dia + mes + anY
unitat = suma % 10
print("unitat =", unitat)
desena = (suma // 10) % 10
print("desena =", desena)
centena = (suma // 100) % 10
print("centena =", centena)
miller = (suma // 1000) % 10
print("miller =", miller)

suma2 = miller + desena + centena + unitat
unitat2 = suma2 % 10
print("unitat2 =", unitat2)
desena2 = (suma2 // 10) % 10
print("desena2 =", desena2)

numero_magic = desena2 + unitat2
print("el número màgic és =", numero_magic)