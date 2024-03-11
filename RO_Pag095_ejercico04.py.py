#RO_Pag095_ejercicio04.py

from math import*

print("introdueix un número de dos xifres:", end="")
numero=int(input())

numero1= numero // 10
numero2= numero % 10

numerosuma = numero1 + numero2

s = numerosuma % 2
if s == 0:
    print("número parell")
else:
    print("número imparell")

