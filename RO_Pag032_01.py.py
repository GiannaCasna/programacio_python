#RO_Page032_01

r= float(input("radi= "))
a= float(input("altura= "))
pi= 3.1416

if a < r:
    volum= pi * r * r * a
    print("volum = ", volum)

else:
    area = 2 * pi * r *( r + a )
    print("area = ", area)

