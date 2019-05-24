nbHabitants=int(input())
listeRevenus=[0]*nbHabitants

for numHabitants in range(nbHabitants) :
   revenu=int(input())
   listeRevenus[numHabitants]=revenu
   
listeRevenus.sort()
             
if nbHabitants%2==1 :
   moyenneImpaire=(nbHabitants-1)//2
   print(listeRevenus[moyenneImpaire])
else :
   moyennePaire=nbHabitants//2
   print((listeRevenus[moyennePaire-1]+(listeRevenus[moyennePaire]))/2)
