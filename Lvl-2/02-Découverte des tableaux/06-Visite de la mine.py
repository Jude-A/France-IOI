nbDeplacements=int(input())
deplacementsIn=[0,2,1,3,5,4]
deplacementsOut=[0]*nbDeplacements
compteurFinal=nbDeplacements

for loop in range(nbDeplacements) :
   deplacements=int(input())
   deplacementsOut[loop]=deplacementsIn[deplacements]
   
for loop in range(nbDeplacements) :
   compteurFinal-=1
   print(deplacementsOut[compteurFinal])
