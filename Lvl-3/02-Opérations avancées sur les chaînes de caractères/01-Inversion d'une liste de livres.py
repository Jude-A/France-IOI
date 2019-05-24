nbLivres=int(input())
listeLivres=[""]*nbLivres

for i in range(nbLivres):
    listeLivres[i]=input()

for i in range(nbLivres-1,-1,-1):
    print(listeLivres[i])
