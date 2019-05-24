nbMots=int(input())
motsAutreSens=[""]*nbMots

for i in range(nbMots):
    motLang1, motLang2 = input().split(" ")
    motsAutreSens[i]=motLang2+" "+motLang1

motsAutreSens.sort()

for i in range(nbMots):
    print(motsAutreSens[i])
