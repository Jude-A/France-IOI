minimum=11

def min2(nb1,nb2) :
      if nb1<nb2 :
         return nb1
      else :
         return nb2

for loop in range(5) :
   nb1=int(input())
   nb2=int(input())
   if min2(nb1,nb2)<minimum :
      minimum=min2(nb1,nb2)   

print(minimum)

