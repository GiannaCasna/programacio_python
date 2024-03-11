#Exercici02_challenge.py

print("Introdueix un any:")
x = int(input())

a = x % 19

b = x % 14

c = x % 7

d = (19*a + 24) % 30

e =  (2*b + 4*c + 6*d + 5) % 7

f = 22 + d + e

if f > 30:
    f = f - 30
    print("El dia de diumenge de Pasqua és: ", f, "d'abril.")
else:
    print("El dia de diumenge de Pasqua és: ", f, "de març.")
