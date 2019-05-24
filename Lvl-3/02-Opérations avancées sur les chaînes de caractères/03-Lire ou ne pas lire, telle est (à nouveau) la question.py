nbLivres=int(input())
listeLivres=[""]*nbLivres

for i in range(nbLivres):
    listeLivres[i]=input()
    
dernierLivreLu=listeLivres[0]
print(dernierLivreLu)

for i in range(1,nbLivres):
    u=0
    livrePris=listeLivres[i]
    while(dernierLivreLu[u]==livrePris[u]):
          u+=1
    if dernierLivreLu[u]<livrePris[u]:
        print(livrePris)
        dernierLivreLu=livrePris

'''
-----CODE FRANCE-IOI------
BIEN MEILLEUR, CAR JE PARCOURAIS LES TITRES LETTRES PAR LETTRES POUR TROUVER LA
PREMIERE DIFF, ALORS QUE > SUFFIT

nbLivres = int(input())
plusGrandTitre = ""
for loop in range(nbLivres):
   titreLivre = input()
   if titreLivre > plusGrandTitre:
      plusGrandTitre = titreLivre
      print(titreLivre)
'''
