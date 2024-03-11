#RO_Pag096_ejercicio013.py

from math import*

print("Hores treballades per el Emilio:")
eh = float(input())
print("Diners per hora treballada per el Emilio:")
edh = float(input())
print("Descomptes (Emilio) en %:")
d_e = float(input())

print("Hores treballades per el Pedro:")
ph = float(input())
print("Diners per hora treballada per el Pedro:")
pdh = float(input())
print("Descomptes (Pedro) en %:")
d_p = float(input())

print("Hores treballades per el Joan:")
jh = float(input())
print("Diners per hora treballada per el Joan:")
jdh = float(input())
print("Descomptes (Joan) en %:")
d_j = float(input())

salari_e = (eh * edh) / (100 - d_e)
print("Salari de l'Emilio =", salari_e)
salari_p = (ph * pdh) / (100 - d_p)
print("Salari d'en Pedro =", salari_p)
salari_j = (jh * jdh) / (100 - d_j)
print("Salari d'en Joan =", salari_j)

if salari_e > salari_p and salari_e > salari_j:
    print("L'Emilio té el salari més alt")
elif salari_p > salari_j and salari_p > salari_e:
    print("El Pedro té el salari més alt")
elif salari_j > salari_e and salari_j > salari_p:
    print("El Joan té el salari més alt")
elif salari_e == salari_p and salari_p == salari_j:
    print("Tots tres tenen el mateix salari")

if salari_e == salari_p:
    print("L'Emilio i el Pedro tenen el mateix salari =", salari_e)
elif salari_p == salari_j:
    print("El Pedro i el Joan tenen el mateix salari =", salari_p)
elif salari_j == salari_e:
    print("El Joan i l'Emilio tenen el mateix salari =", salari_j)
