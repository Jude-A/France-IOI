from robot import *

nbAllersRetour=1

for loop in range(10) :
   for loop in range(nbAllersRetour) :
      droite()
   ramasser()
   for loop in range(nbAllersRetour) :
      gauche()
   deposer()
   nbAllersRetour+=1
