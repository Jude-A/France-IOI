mainJoueur1=input()
mainJoueur2=input()
scoreJoueur1=0
scoreJoueur2=0
égalité=0

mini=min(len(mainJoueur1),len(mainJoueur2))

for loop in range(mini) :
   if mainJoueur1[loop]<mainJoueur2[loop] :
      scoreJoueur1+=1
      break
   elif mainJoueur1[loop]>mainJoueur2[loop] :
      scoreJoueur2+=1
      break
   else :
      égalité+=1
      
if scoreJoueur1>scoreJoueur2 or (scoreJoueur1==scoreJoueur2 and len(mainJoueur2)<len(mainJoueur1)) :
   print(1)
elif scoreJoueur1<scoreJoueur2 or (scoreJoueur1==scoreJoueur2 and len(mainJoueur1)<len(mainJoueur2)) :
   print(2)
else :   
   print("=")
   
print(égalité)

