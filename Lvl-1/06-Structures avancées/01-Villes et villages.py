nbVilles=int(input())
totalVilles=0

for loop in range(nbVilles) :
   population=int(input())
   if population>10000 :
      totalVilles+=1

print(totalVilles)
