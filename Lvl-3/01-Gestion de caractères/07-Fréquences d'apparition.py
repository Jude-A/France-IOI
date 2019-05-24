nbApparitions=[0]*26
texte=input().lower()
compteLettres=0

for lettre in range(len(texte)):
    numLettre=ord(texte[lettre])-ord("a")
    if numLettre>=0 and numLettre<=25:
        nbApparitions[numLettre]+=1
        compteLettres+=1

for lettre in nbApparitions:
    print(lettre/compteLettres)
