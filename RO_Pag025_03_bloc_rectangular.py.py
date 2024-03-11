#RO_Pag025_03_bloc_rectangular

altura=float(input("dimensions de l'alçada= ")) #varialbes
base=float(input("dimensions de l'amplada= "))
profunditat=float(input("dimensions de la profunditat= "))

area= (altura * base) + (base * profunditat) + (profunditat * altura)#càlculs
volum= altura * base * profunditat

print("area total= ", area)
print("volum total= ", volum)
