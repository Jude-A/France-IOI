nbCharrettes=int(input())
poidsTotal=0
indexCharrette=[0]*nbCharrettes

for numCharrettes in range(nbCharrettes) :
   poids=float(input())
   indexCharrette[numCharrettes]+=poids
   poidsTotal+=poids

diviseur=poidsTotal/nbCharrettes

for numCharrettes in range(nbCharrettes) :
   indexCharrette[numCharrettes]=diviseur-indexCharrette[numCharrettes]
   print(indexCharrette[numCharrettes])
