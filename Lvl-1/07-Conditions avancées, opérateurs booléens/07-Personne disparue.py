numDisparu=int(input())
tailleRegistre=int(input())
parti=False

for loop in range(tailleRegistre) :
   numRegistre=int(input())
   if numRegistre==numDisparu :
      parti=True

if parti :
   print("Sorti de la ville")
else :
   print("Encore dans la ville")
