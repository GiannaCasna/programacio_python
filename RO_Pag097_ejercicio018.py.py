#RO_Pag097_ejercicio018.py

from math import*

print("Introdueix el teu pes en kg:")
p = float(input())

print("Introdueix la teva alçada en metres:")
a = float(input())

IMC = p / pow (a, 2)

if IMC <= 20:
    print("Desnutrit!!")
elif IMC>20 and IMC<25:
    print("Normal!")
elif IMC>=25 and IMC<30:
    print("Sobrepes!")
elif IMC>=30 and IMC<35:
    print("Obesitat grau 1!")
elif IMC>=35 and IMC<40:
    print("Obesitat grau 2!")
elif IMC>=40:
    print("Obesitat grau 3!")
