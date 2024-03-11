#Exercici03_challenge.py

#APARTAT a)
ce = 4.187
p = 1000
x = 0.75 #dimensió de la banyera en metres
y = 0.125 #dimensió de la banyera en metres
t = 20 #increment de la temperatura = 35ºC - 15ºC = 20ºC
h = 1 #ALÇÀRIA.
#Com que l'enunciat en diu que ha de ser en funció de làlçària, he decidi posar 1 ja que d'aquesta manera no efecte, però si la vols canviar, pots fer-ho. 
#Sóc conscient de que m'he deixat alguna dada a la fòrmula.
E = ce * p * x * y * t * h
print("L'energia necessària per escalfar l'aigua de la banyera en funció de l'alçària és= ", E)

#APARTAT b)
#Les dimensions de la banyera, en aquest cas l'alçària, els he posat directament en m, ja que treballo en el S.I.
r = 0.2
u = 0.25
i = 0.3
j = 0.35
s = 0.4

E1 = E * r
print("L'energia necessària per escalfar l'aigua de la banyera amb un alçada de 200mm és= ", E1)
E2 = E * u
print("L'energia necessària per escalfar l'aigua de la banyera amb un alçada de 250mm és= ", E2)
E3 = E * i
print("L'energia necessària per escalfar l'aigua de la banyera amb un alçada de 300mm és= ", E3)
E4 = E * j
print("L'energia necessària per escalfar l'aigua de la banyera amb un alçada de 350mm és= ", E4)
E5 = E * s
print("L'energia necessària per escalfar l'aigua de la banyera amb un alçada de 400mm és= ", E5)

#APARTAT c)







