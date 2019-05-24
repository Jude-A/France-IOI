nbCotes=int(input())
totalPos=0
totalNeg=0

for loop in range(nbCotes) :
   denivelé=int(input())
   if denivelé>0 :
      totalPos+=denivelé
   else :
      totalNeg+=denivelé

print(totalPos)
print(-totalNeg)
