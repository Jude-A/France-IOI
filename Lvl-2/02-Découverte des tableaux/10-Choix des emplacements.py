nbEmplacements=int(input())
listeMarchands=[0]*nbEmplacements

for emplacements in range(nbEmplacements) :
   numMarchand=int(input())
   listeMarchands[numMarchand]=emplacements
   
for idMarchand in range(nbEmplacements) :
   print(listeMarchands[idMarchand])
