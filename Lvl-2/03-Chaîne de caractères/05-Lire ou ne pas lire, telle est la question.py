nbLivres=int(input())
longueurMax=0

for idLivre in range(nbLivres) :
   titreLivre=input()
   if len(titreLivre)>longueurMax :
      print(titreLivre)
      longueurMax=len(titreLivre)
