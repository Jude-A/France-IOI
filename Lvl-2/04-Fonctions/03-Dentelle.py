def ligneDe(symbole,nbColonnes) :
   for loop in range(nbColonnes) :
      print(symbole, end="")
   print()
      
nbColonnes=int(input())
ligneDe("X",nbColonnes)
ligneDe("#",nbColonnes)
ligneDe("i",nbColonnes)
