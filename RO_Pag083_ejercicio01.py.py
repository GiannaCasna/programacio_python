#RO_Pag083_ejercicio01

from math import*

print("introdueix el nombre de dies:")
dies= int(input())

anys = dies // 365
dies_restants = dies % 365

mesos = dies_restants // 30
dies_mesos = mesos * 30

dies_finals = dies_restants - dies_mesos

print("anys=", anys)
print("mesos=", mesos)
print("dies=", dies_finals)



