#RO_Pag96_ejercicio06.py

from math import*

print("quantitat de kWh=")
kwh = float(input())

print("preu per kW hora=")
preu = float(input())

if kwh > 700:
    preu = preu * 1.05
    
cost = preu * kwh

print("cost total=", cost)

    
