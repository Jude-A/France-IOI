dateDebut1=int(input())
dateFin1=int(input())
dateDebut2=int(input())
dateFin2=int(input())

if (dateDebut2>=dateDebut1 and dateDebut2<=dateFin1) or (dateFin2>=dateDebut1 and dateFin2<=dateFin1) or (dateDebut1>=dateDebut2 and dateDebut1<=dateFin2) :
   print("Amis")
else :
   print("Pas amis")
