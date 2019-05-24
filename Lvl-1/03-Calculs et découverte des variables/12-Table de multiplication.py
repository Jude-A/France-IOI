nbLignes=1
nbColonnes=1
nb=1

for loop in range(20) :
   for loop in range(20) :
      print(nbColonnes*nbLignes*nb, end=" ")
      nbLignes+=1
   print()
   nbLignes=1
   nbColonnes+=1
   nb=1
