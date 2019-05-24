quantité=[9,5,12,15,7,42,13,10,1,20]
coutTotal=0

for ingrédient in range(10) :
   poids=int(input())
   coutTotal+=poids*quantité[ingrédient]
   
print(coutTotal)
   
