#RO_Pag098_ejercicio022.py

print("Introdueix tres números:")
print("Número x= ")
x = int(input())
print("Número a= ")
a = int(input())
print("Número b= ")
b = int(input())

if a > b and b > x:
    print ("El número x és el més petit")
elif b > a and a > x:
    print ("El número x és el més petit")
elif x > b and x < a:
    print("El número x és més gran que b però més petit de a")
elif x > a and x < b:
    print("El número x és més gran que a però més petit de b")
elif x > a and x > b:
    print("El número x és el més gran de tots tres")

    


    
     