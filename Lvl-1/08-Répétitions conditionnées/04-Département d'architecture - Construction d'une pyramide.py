maxPierres=int(input())
pierresUtilisées=0
cotés=0

while maxPierres!=0 and pierresUtilisées+(cotés+1)*(cotés+1)<=maxPierres :
   cotés+=1
   pierresUtilisées+=cotés*cotés
   
print(cotés)
print(pierresUtilisées)
