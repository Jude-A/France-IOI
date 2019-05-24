dateDébut=int(input())
dateFin=int(input())
nbInvités=int(input())
nbSuspects=0

for loop in range(nbInvités) :
   dateArrivée=int(input())
   dateDépart=int(input())
   innocent=(dateDépart<dateDébut) or (dateArrivée>dateFin)
   if not innocent :
      nbSuspects+=1
     
print(nbSuspects)
   
