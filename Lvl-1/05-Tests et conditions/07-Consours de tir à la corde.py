nbJoueurs=int(input())
poidsEquipeA=0
poidsEquipeB=0

for loop in range(nbJoueurs) :
   equipierA=int(input())
   poidsEquipeA+=equipierA
   equipierB=int(input())
   poidsEquipeB+=equipierB
   
if poidsEquipeA>poidsEquipeB :
   print("L'équipe 1 a un avantage")
else :
   print("L'équipe 2 a un avantage")
   
print("Poids total pour l'équipe 1 :",poidsEquipeA)
print("Poids total pour l'équipe 2 :",poidsEquipeB)
