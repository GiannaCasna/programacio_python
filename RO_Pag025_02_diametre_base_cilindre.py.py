#RO_Pag025_01_diametre_base_cilindre

volum = float(input("volum= ")) #variables
altura = float(input("altura= "))
pi = 3.1416

volum = volum / 1000 # per passar de litres a m3.
diametre = (volum * 4/ pi * altura) **0.5

print("volum = ", volum)
print("diametre = ", diametre)
