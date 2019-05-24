from robot import *

for loop in range(9) :
   haut()
   
droite()

for loop in range(4) :
   for loop in range(8) :
      bas()
   droite()
   for loop in range(8) :
      haut()
   droite()
   
for loop in range(9) :
   bas()
for loop in range(9) :
   gauche()
