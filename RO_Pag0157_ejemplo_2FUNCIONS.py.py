#RO_Pag0157_ejemplo_2FUNCIONS.py

def f(x):
    y = 2*x**2 + 1
    return y
def g(x):
    y = 3*x**3 + 5
    return y
    
for i in range (1, 5):
    y = f(i)
    print(i, y)

print(" ")

for i in range (1, 5):
    y = g(i)
    print(i, y)
    
    