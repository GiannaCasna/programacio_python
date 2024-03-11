#RO_Pag0147_ejercicio014_articles.py

articles = [454, 785, 1000, 2343]
print("Diners que disposa per comprar: ")
diners = int(input())
articles_comprar= 0

for n in range (0, 4):
    if diners >= articles[n]:
        articles_comprar = articles_comprar + 1
        print("podem comprar", diners//articles[n], "unitats de l'article", n+1)
    if n == len(articles)-1:
        print("articles que podem comprar = ", articles_comprar)

while i < len(articles):
    