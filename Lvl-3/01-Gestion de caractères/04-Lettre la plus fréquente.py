texte=input()
texteMaj=texte.upper()
listeLettres=[0]*26

for i in range(len(texteMaj)):
    ordASCII=ord(texteMaj[i])
    if ordASCII>=65 and ordASCII<=90 :
        listeLettres[ordASCII-65]+=1

maxListe=max(listeLettres)
lettreMax=chr(listeLettres.index(maxListe)+65)
print(lettreMax)
