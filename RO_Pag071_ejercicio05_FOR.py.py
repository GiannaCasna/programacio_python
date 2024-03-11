#RO_Pag071_ejercicio05_FOR

#APARTAT a)
print("introdueix el valor de cada dipòsit menusal:")
p = float(input())

print("introdueix el valor de l'interes mansual:")
x = float(input())

print("nombre de dipòsits mensuals efectuats:")
n = int(input())

mes = p + x*p
print("capital mes 1= ", mes)

for i in range (2, n):
    mes_seguent= (mes + p) + x*(mes + p)
    mes = mes_seguent

mes_seguent = (mes + p)
print("capital final= ", mes_seguent)

    