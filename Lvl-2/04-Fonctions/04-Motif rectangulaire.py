def feuille(lignes,colonnes,motif) :
   for loop in range(lignes) :
      for loop in range(colonnes) :
         print(motif,end="")
      print()
      
nbLignes=int(input())
nbColonnes=int(input())
motif=input()

feuille(nbLignes,nbColonnes,motif)
