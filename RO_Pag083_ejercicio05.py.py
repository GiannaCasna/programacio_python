#RO_Pag083_ejercicio05

print("quantitat de dolars=")
d = int(input())

cien = d // 100
residuo = d % 100

cincuenta = residuo // 50
residuo = residuo % 50

veinte = residuo // 20
residuo = residuo % 20

diez = residuo // 10
residuo = residuo % 10

cinco = residuo // 5
uno = residuo % 5

print("billet de 100:", cien)
print("billet de 50:", cincuenta)
print("billet de 20:", veinte)
print("billet de 10:", diez)
print("billet de 5:", cinco)
print("billet d'1:", uno)