nbLivres=int(input())
listeLivres=[""]*nbLivres

for i in range(nbLivres):
    listeLivres[i]=input()

listeLivres.sort()

for i in range(nbLivres):
    print(listeLivres[i])
