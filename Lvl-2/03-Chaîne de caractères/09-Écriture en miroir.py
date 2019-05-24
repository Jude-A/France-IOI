nbLignes=int(input())

for loop in range(nbLignes) :
   texte=input()
   for loop in range(len(texte)-1,-1, -1) :
      print(texte[loop], end="")
   print()
