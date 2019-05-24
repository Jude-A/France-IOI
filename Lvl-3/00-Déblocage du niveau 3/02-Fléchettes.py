#Fonction pour dessiner une ligne
def dessinerLigne(nbColonnes,lettre) :
    for idColonne in range(nbColonnes) :
        print(lettre,end="")

nbLettres=int(input())

#Variable déterminant le nb de colonnes et de lignes dans la cible
nbColonnes=2*nbLettres-1

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#1ère moitié de cible
for idLigne in range(nbLettres) :
    if idLigne>0 :
        for i in range(idLigne) :
            print(alphabet[i],end="")
    dessinerLigne(nbColonnes,alphabet[idLigne])
    if idLigne>0 :
        for i in range(idLigne-1,-1,-1) :
            print(alphabet[i],end="")
    nbColonnes-=2
    print()

#Remet le compteur de colonnes pour afficher le bon nombre de lettres dans la ligne
nbColonnes+=4

#Seconde moitié de cible
for idLigne in range(nbLettres-2,-1,-1) :
    if idLigne>0 :
        for i in range(idLigne) :
            print(alphabet[i],end="")
    dessinerLigne(nbColonnes,alphabet[idLigne])
    if idLigne>0 :
        for i in range(idLigne-1,-1,-1) :
            print(alphabet[i],end="")
    nbColonnes+=2
    print()
