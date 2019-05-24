def dessinLignes(nbColonnes,symbole) :
   for loop in range(nbColonnes) :
      print(symbole,end="")
   print()

def dessinRectangle(nbLignes, nbColonnes, symbole) :
   dessinLignes(nbColonnes, symbole)
   if nbColonnes>1 :
      for loop in range(nbLignes-2) :
         print(symbole, end="")
         for loop in range(nbColonnes-2) :
            print(" ", end="")
         print(symbole)
   else :
      for loop in range(nbLignes-2) :
         print(symbole)
   dessinLignes(nbColonnes, symbole)
      
def dessinTriangle(nbLignes,symbole) :
   print(symbole)
   for loop in range(nbLignes-2) :
      print(symbole, end="")
      for boucle in range(loop) :
         print(" ", end="")
      print(symbole)
   dessinLignes(nbLignes,symbole)
      
dessinLignes(int(input()),"X")
print()
dessinRectangle(int(input()), int(input()), "#")
print()
dessinTriangle(int(input()), "@") 
