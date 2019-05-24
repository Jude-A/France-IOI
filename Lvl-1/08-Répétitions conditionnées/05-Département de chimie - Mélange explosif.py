totalMesures=int(input())
tempMin=int(input())
tempMax=int(input())
nbMesures=1
temp=int(input())

while nbMesures<=totalMesures and temp>=tempMin and temp<=tempMax :
   print("Rien à signaler")
   if (nbMesures!=totalMesures) :
      temp=int(input())
   nbMesures+=1
   
if temp<tempMin or temp>tempMax :
   print("Alerte !!")
