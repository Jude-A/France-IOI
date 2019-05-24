nbOpérations=int(input())
stock=[0]*11

for loop in range(nbOpérations) :
   ingrédient=int(input())
   stock[ingrédient]+=int(input())
   
for ingrédient in range(1,11) :
   print(stock[ingrédient])
