#RO_Pag097_ejercicio020.py

print("Introdueix les dimensions d'un bloc rectangular:")
print("Amplada =")
a = float(input())
print("Altura =")
h = float(input())
print("Profunditat =")
p = float(input())

if a > h and a > p:
    aa = a * h
    print("L'àrea més gran és:", aa)
elif h > a and h > p:
    ah = h * a
    print("L'àrea més gran és:", ah)
elif p > a and p > h:
    ap = p * a
    print("L'àrea més gran és:", ap)
