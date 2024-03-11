#RO_Pag083_ejercicio02.py

from math import*

print("nombre de dies=")
dies_inici = int(input())

mesos = dies_inici // 30
dies_restants = dies_inici % 30

setmanes = dies_restants // 7
dies = dies_restants % 7

print("nombre de mesos=", mesos)
print("nombre de setmanes=", setmanes)
print("nombre de dies=", dies)
