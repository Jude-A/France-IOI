position=int(input())
nbVillages=int(input())
totalVillages=0

for loop in range(nbVillages) :
   positionVillage=int(input())
   if (positionVillage-position)<=50 and (positionVillage-position)>=(-50) :
      totalVillages+=1
      
print(totalVillages)
