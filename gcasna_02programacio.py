#gcasna_02programacio.py

d = int(input("dia del teu neixament: "))
m = int(input("mes del teu neixament: "))
a = int(input("any del teu neixment: "))

p = d + m + a
l = p // 100
s = p % 100
i = l //10
n = s //10
v = l % 10
o = s %10
u = i + n + v + o

k = u // 10
uu = k % 10
print(u, uu)
nn = u + uu
print("El número del tarot és: ", nn)





