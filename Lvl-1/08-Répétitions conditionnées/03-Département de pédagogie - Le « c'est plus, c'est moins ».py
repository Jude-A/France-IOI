nbSecret=int(input())
nbProposition=int(input())
nbEssais=1

while nbProposition!=nbSecret :
   if nbProposition<nbSecret :
      print("c'est plus")
      nbEssais+=1
   else :
      print("c'est moins")
      nbEssais+=1
   nbProposition=int(input())
   
print("Nombre d'essais nécessaires :")
print(nbEssais)
