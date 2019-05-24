nbPlaces=int(input())
nbChgmtsPositions=int(input())
listePositions=[0]*nbPlaces

for personne in range(nbPlaces) :
   listePositions[personne]=int(input())

for loop in range(nbChgmtsPositions) :
   position1=int(input())
   position2=int(input())
   tempPosition2=listePositions[position2]
   listePositions[position2]=listePositions[position1]
   listePositions[position1]=tempPosition2
   
for loop in range(nbPlaces) :
   print(listePositions[loop])
