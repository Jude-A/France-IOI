debutInter=int(input())
finInter=int(input())
nbPersonnes=int(input())
personnesDansIntervalle=0

for loop in range(nbPersonnes) :
   dateArrivee=int(input())
   if (dateArrivee>=debutInter) and (dateArrivee<=finInter) :
      personnesDansIntervalle+=1
      
print(personnesDansIntervalle)
