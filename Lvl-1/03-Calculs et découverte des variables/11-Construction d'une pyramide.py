côté=17
nbTotal=côté*côté*côté

for loop in range(8) :
   côté-=2
   nbTotal=nbTotal+côté*côté*côté
print(nbTotal)
