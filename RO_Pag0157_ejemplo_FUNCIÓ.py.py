#RO_Pag0157_ejemplo_FUNCIÓ.py

def f(x):
    y = 2*x**2 + 1
    return y

#Programa que utilitza la funció f

for i in range (1,5):
    y = f(i)
    print(i, y)
    