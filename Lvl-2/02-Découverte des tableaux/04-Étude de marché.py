nbProduits=int(input())
nbPersonnes=int(input())
listeProduit=[0]*nbProduits

for loop in range(nbPersonnes) :
   produitPref=int(input())
   listeProduit[produitPref]+=1
   
for produitPref in range(nbProduits) :
   print(listeProduit[produitPref])
