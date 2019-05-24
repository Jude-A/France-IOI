nbLivres,nbJours=map(int,input().split(" "))
dateRendu=[0]*nbLivres

for iJour in range(nbJours) :
   nbClients=int(input())
   for iCLient in range(nbClients) :
      indiceLivre, duree=map(int,input().split(" "))
      if dateRendu[indiceLivre]<=iJour :
         print(1)
         dateRendu[indiceLivre]=iJour+duree
      else :
         print(0)
