#RO_pàg.033_PROVA_01

a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))
d= int(input("d= "))

if (a > 0) or (b > a) and (c != d) :
    a = c
    b = 0
else:
    c = d + c
    if c == 0 : 
        c = c + b
    else:
        c = c - a
    b= a + c + d

print("a= ", a)
print("b= ", b)
print("c= ", c)
print("d= ", d)