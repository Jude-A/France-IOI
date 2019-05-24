nbPersonnes=int(input())
totalPersonnes=0
record=0

for loop in range(2*nbPersonnes) :
   lectureAccueil=int(input())
   if lectureAccueil<0 :
      totalPersonnes-=1
   else :
      totalPersonnes+=1
   if totalPersonnes>record :
      record=totalPersonnes
      
print(record)
