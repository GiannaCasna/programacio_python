#RO_Page032_03

t= float(input("temperatura= "))
print("escull 1 o 2= ")
p= float(input("p= "))

if p == 1:
    tc= 5 / 9 *(t - 32)
    print("tc= ", tc)

else:
    tf = 32 + 9 * t / 5
    print("tf= ", tf)
    
