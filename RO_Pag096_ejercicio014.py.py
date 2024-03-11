#RO_Pag096_ejercicio014.py

print("Introdueix el diàmetre d'un forat:")
d = float(input())

print("Introdueix les dimensions d'un bloc rectangular:")
print("Amplada=", end="")
a = float(input())

print("Altura=", end="")
h = float(input())

print("Profunditat=", end="")
p = float(input())

if a < d:
    print("Si que pot passar pel forat!")
elif h < d:
    print("Si que pot passar pel forat!")
elif p < d:
    print("Si que pot passar pel forat!")
else:
    print("No pot passar!!")