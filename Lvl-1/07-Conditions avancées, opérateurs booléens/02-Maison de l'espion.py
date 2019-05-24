xMin=int(input())
xMax=int(input())
yMin=int(input())
yMax=int(input())
nbMaisons=int(input())
totalDansZone=0

for loop in range(nbMaisons) :
   xMaison=int(input())
   yMaison=int(input())
   if (xMaison>=xMin) and (xMaison<=xMax) and (yMaison>=yMin) and (yMaison<=yMax) :
      totalDansZone+=1
      
print(totalDansZone)
