#RO_Pag0105_ejemplo_WHILE_ulam.py

"Seqüència d'Ulam"
x = int(input("Introdueix la dada inicial"))
while x>1:
    if x%2 == 0:
        x = x//2
    else:
        x = 3*x+1
    print(x)
    
    