def compteNombreEnTete(liste,nb) :
   nbEnTete=0
   maximum=max(liste)
   for i in range(nb) :
      if liste[i]==maximum :
         nbEnTete+=1
   return nbEnTete

nbGrenouilles=int(input())
nbTours=int(input())

compteEnTete=[0]*(nbGrenouilles)
listeDistances=[0]*(nbGrenouilles)

totalDistance=0

for i in range(nbTours-1) :
   numGrenouille,distance=map(int,input().split(" "))
   totalDistance=listeDistances[numGrenouille-1]+distance
   if totalDistance>max(listeDistances) :
      compteEnTete[numGrenouille-1]+=1
   elif totalDistance<max(listeDistances) and compteNombreEnTete(listeDistances,nbGrenouilles)==1 :
      compteEnTete[listeDistances.index(max(listeDistances))]+=1
   listeDistances[numGrenouille-1]+=distance
  
print(compteEnTete.index(max(compteEnTete))+1)
