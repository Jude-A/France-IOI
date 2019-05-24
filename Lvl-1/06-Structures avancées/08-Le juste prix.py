nbMarchands=int(input())
positionMarchand=1
prixMin=1000000
marchandMoinsCher=1

for loop in range(nbMarchands) :
   prix=int(input())
   if prix<=prixMin :
      marchandMoinsCher=positionMarchand
      prixMin=prix
   positionMarchand+= 1
   
print(marchandMoinsCher)   
