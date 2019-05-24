def suite(nb) :
   if nb%2==0 :
      nb=nb//2
      return nb
   else :
      nb=nb*3+1
      return nb
      
nb=int(input())

while nb>1 :
   print(suite(nb),end=" ")
   nb=suite(nb)
