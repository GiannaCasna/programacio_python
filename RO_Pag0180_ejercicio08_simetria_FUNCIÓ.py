#RO_Pag0180_ejercicio08_simetria_FUNCIÓ.py

#Escriu una funció que rebi un nombre enter i determini si és simètric
#és a dir, si els digits oposats al voltant del centre són iguals.

def sim(x):
    f = 0
    a = x // 1000
    b = (x - (a * 1000)) // 100
    c = (x - (a * 1000) - (b * 1000)) // 10
    d = x % 10


    
    
    return (f) #mirem si els primers num. són iguals a zero i dsp igualem els elements per veure si son simètrics.
