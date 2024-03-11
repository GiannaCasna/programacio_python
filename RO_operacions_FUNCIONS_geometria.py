# RO_operacions_FUNCIONS_geometria.py

from math import*
def quadrat (a):
    P = 4*a
    A = a**2
    print("perímetre = ", P)
    print("àrea = ", A)

def triangle (a, b, c, h):
    P = a + b + c
    A = (b*h)/2
    print("perímetre = ", P)
    print("àrea = ", A)
    
def rectanlge (a, b):
    P = 2*(b+a)
    A = b*a
    print("perímetre = ", P)
    print("àrea = ", A)
    
def paralelogram (a, b, h):
    P = 2*(b+a)
    A = b*h
    print("perímetre = ", P)
    print("àrea = ", A)
    
def rombo (a, D, d):
    P = 4*a
    A = (D*d)/2
    print("perímetre = ", P)
    print("àrea = ", A)
    
def estel (a, b, d, D):
    P = 2*(b+a)
    A = (D*d)/2
    print("perímetre = ", P)
    print("àrea = ", A)
    
def trapezi (a, b, B, c, h):
    P = B + b + a + c
    A = [(B+b)*h]/2
    print("perímetre = ", P)
    print("àrea = ", A)
    
def cercle (r):
    P = 2*pi*r
    A = pi*r**2
    print("perímetre = ", P)
    print("àrea = ", A)
    
def poligon_regular (a, b, n):
    P = n*b
    A = (P*a)/2
    #a= és l'apotema
    #n = és el número de costats
    print("perímetre = ", P)
    print("àrea = ", A)

def corona_circular (R, r):
    A = pi *(R**2 - r**2)
    print("àrea = ", A)

def sector_circular (R, n):
    A = ((pi*R**2 *n)/ 360)
    print("àrea = ", A)

def cubo (a):
    A = 6*a**2
    V = a**3
    print("àrea = ", A)
    print("volum = ", V)
    
def cilindre (R, h):
    A = (2*pi) * R*(h + R)
    V = pi * R**2 *h
    print("àrea = ", A)
    print("volum = ", V)

def ortoedro (a, b, c):
    A = 2*((a*b) + (a*c) + (b*c))
    V = a*b*c
    print("àrea = ", A)
    print("volum = ", V)

def prisma_recta (P, a, h, AA):
    A = P *(h + a)
    V = AA *h
    #P = és el perímetre de la base
    #AA = és l'àrea de la base
    #a = és l'apotema de la base
    print("àrea = ", A)
    print("volum = ", V)

def cono (R, g, h):
    A = pi*R *(R + g)
    V = ((pi*R**2*h)/3)
    #g = és la generatriz
    print("àrea = ", A)
    print("volum = ", V)

def tronc_de_cono (g, r, R):
    A = pi*[g*(r + R) + r**2 + R**2]
    V = [((pi*h)*(R**2 + r**2 + R*r))/3]
    print("àrea = ", A)
    print("volum = ", V)

def esfera (R):
    A = 4*pi*R**2
    V = (4*pi*R**3)/3
    print("àrea = ", A)
    print("volum = ", V)

def piramide (P, a, aa, AA):
    A = ((P *(a + aa))/2)
    V = ((AA * h)/3)
    #P = és el perímetre de la base
    #AA = és l'àrea de la base
    print("àrea = ", A)
    print("volum = ", V)

def tetraedro_regular (a):
    A = sqrt(3) * a**2
    V = ((sqrt(2) * a**3)/12)
    print("àrea = ", A)
    print("volum = ", V)

def octaedro_regular (a):
    A = 2*sqrt(3)*a**2
    V = ((sqrt(2) * a**3)/3)
    print("àrea = ", A)
    print("volum = ", V)

def tronc_de_piramide (P, PP, A, AA, a, h):
    A = ((P + PP)/2 * a + A + AA)
    V = [((A + AA + sqrt(A*AA)) * h)]/ 3
    #P i PP = són els perímetres de les bases
    #A i AA = són les àrees de les bases
    print("àrea = ", A)
    print("volum = ", V)

def casquet_esferic (h, R):
    A = (2*pi) * R * h
    V = ((pi * h**2 *((3*R)-h))/3)
    print("àrea = ", A)
    print("volum = ", V)

def cuña_esferica (nº, R):
    A = ((4*pi*R**2*nº)/360)
    V = ((4*pi*R**3*nº)/(3*360))
    print("àrea = ", A)
    print("volum = ", V)

def zona_ó_segment_esferic (R, h, r, rr):
    A = (2*pi) * R *h
    V = ((pi*h*(h**2+(3*r**2)+(3*rr**2)))/6)
    print("àrea = ", A)
    print("volum = ", V)
    
#programa principal main
sortida = False
while not sortida:
    print("")
    print("Càlcul de perímetres, àrees i volums")
    print("Escull la figura a calcular:")
    print("1. cuadrat")
    print("2. triangle")
    print("3. rectangle")
    print("4. paralelogram")
    print("5. rombo")
    print("6. estel")
    print("7. trapezi")
    print("8. cercle")
    print("9. polígon_regular")
    print("10. corona_circular")
    print("11. sector_circular")
    print("12. cubo")
    print("13. cilindre")
    print("14. ortoedro")
    print("15. prisma_recta")
    print("16. cono")
    print("17. tronc_de_cono")
    print("18. esfera")
    print("19. piramide")
    print("20. tetraedro_regular")
    print("21. octaedro_regular")
    print("22. tronc_de_piramide")
    print("23. casquet_esfèric")
    print("24. cuña_esfèrica")
    print("25. zona_ó_segment_esferic")
    
opcio = int(input("Escull una opció:"))
if opcio == 1:
    print("Figura escollida: quadrat")
    a = float(input("introdueix el costat a= "))

elif opcio == 2:
    print("Figura escollida: triangle")
    a = float(input("introdueix un dels costats del triangle a= "))
    b = float(input("introdueix la base del triangle b= "))
    c = float(input("introdueix un dels costats del triangle c= "))
    h = float(input("introdueix l'alçada del triangle h= "))

elif opcio == 3:
    print("Figura escollida: rectangle")
    a = float(input("introdueix l'alçada del rectangle a= "))
    b = float(input("introdueix la base del rectangle b= "))

elif opcio == 4:
    print("Figura escollida: paralelogram")
    a = float(input("introdueix un costat del paralelogram a= "))
    b = float(input("introdueix la base del palalelogram b= "))
    h = float(input("introdueix l'alçada del paralelogram a= "))

elif opcio == 5:
    print("Figura escollida: rombo")
    a =float(input("introdueix la mesura d'un costat del rombo a= "))
    d = float(input("introdueix la diagonal petita que talla el rombo d= "))
    D = float(input("introdueix la diagonal gran que talla el rombo D= "))
    
elif opcio == 6:
    print("Figura escollida: estel")
    a = float(input("introdueix el costat petit del cometa a= "))
    b = float(input("introdueix el costat gran del cometa b= "))
    d = float(input("introdueix la diagonal petita que talla el rombo d= "))
    D = float(input("introdueix la diagonal gran que talla el rombo D= "))

elif opcio == 7:
    print("Figura escollida: trapezi")
    a = float(input("introdueix un costat del trapezi a= "))
    c = float(input("introdueix un costat del trapezi c= "))
    b = float(input("introdueix la base de dalt del trapezi b= "))
    B = float(input("introdueix la base del trapezi B= "))
    h = float(input("introdueix l'alçada del trapezi h= "))
    
elif opcio == 8:
    pritn("Figura escollida: cercle")
    r = float(input("introdueix el radi de la circumferència r= "))

elif opcio == 9:
    print("Figura escollida: polígon_regular")
    a = float(input("introdueix l'apotema del polígon_regular a= "))
    b = float(input("introdueix la mesura d'un dels costats del polígon b= "))
    n = float(input("introdueix el nobmre de costat que té el polígon n= "))
    
elif opcio == 10:
    print("Figura escollida: corona_circular")
    r = float(input("introdueix el radi des del centre fins la corona r= "))
    R = float(input("introdueix el radi des del centre fins a l'exterior R= "))

elif opcio == 11:
    print("Figura escollida: sector_circular")
    R = float(input("introdueix el radi R= "))
    n = float(input("introdueix els gruas de l'angle nº= "))

elif opcio == 12:
    print("Figura escollida: cubo")
    a = float(input("introdueix la mesura d'un costat del cub a= "))
    
elif opcio == 13:
    print("Figura escollida: cilindre")
    R = float(input("introdueix el radi del cilindre R= "))
    h = float(input("introdueix l'alçada del cilindre h= "))

elif opcio == 14:
    print("Figura escollida: ortoedro")
    a = float(input("introdueix l'amplada de l'ortoedro a= "))
    b = float(input("introdueix la profunditat de l'ortoedro b= "))
    c = float(input("introdueix l'alçada de l'ortoedro c= "))
elif opcio == 15:
    print("Figura escollida: prisma_recta")
    a =
    h =
    AA =
    P =
    
elif opcio == 16:
    print("Figura escollida: cono")
    R =
    g =
    
elif opcio == 17:
    print("Figura escollida: tronc_de_cono")
    r =
    h =
    g =
    R =
    
elif opcio == 18:
    print("Figura escollida: esfera")
    R =
    
elif opcio == 19:
    print("Figura escollida: piramide")
    a =
    aa =
    AA =
    P =

elif opcio == 20:
    print("Figura escollida: tetraedro_regular")
    a =
    
elif opcio == 21:
    print("Figura escollida: octaedro_regular")
    a =
    
elif opcio == 22:
    print("Figura escollida: tronc_de_piramide")
    P =
    PP =
    AA =
    AAA =
    h =
    a =

elif opcio == 23:
    print("Figura escollida: casquet_esfèric")
    h =
    R =
    
elif opcio == 24:
    print("Figura escollida: cuña_esfèrica")
    R =
    n =
    
elif opcio == 25:
    print("Figura escollida: zona_ó_segment_esfèric")
    R =
    r =
    rr =
    h =