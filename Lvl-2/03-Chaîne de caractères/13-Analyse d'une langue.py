lettre=input()
nbLignes=int(input())
compte=0

for loop in range(nbLignes) :
   texte=input()
   for loop in range(len(texte)) :
      if texte[loop]==lettre :
         compte+=1
      
print(compte)
