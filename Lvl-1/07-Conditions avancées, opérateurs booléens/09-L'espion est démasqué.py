nbPersonnes=int(input())

for loop in range(nbPersonnes) :
   taille=int(input())
   age=int(input())
   poids=int(input())
   aCheval=int(input())
   aCheveuxBruns=int(input())   
   indice=0
   if (taille>=178 and taille<=182) :
      indice+=1
   if (age>=34) :
      indice+=1
   if (poids<70) :
      indice+=1
   if (aCheval==0) :
      indice+=1
   if (aCheveuxBruns==1) :
      indice+=1
   if (indice==5) :
      print("Très probable")
   elif (indice==3 or indice==4) :
      print("Probable")
   elif (indice==0) :
      print("Impossible")
   else :  
      print("Peu probable")
