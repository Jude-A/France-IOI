nbLignes, nbMots = map(int, input().split(" "))
histogramme = [0] * 101
for loop in range(nbLignes):
   mots = input().split(" ")
   for idMot in range(nbMots):
      longueur = len(mots[idMot])
      histogramme[longueur] = histogramme[longueur] + 1
for longueur in range(101):
   if histogramme[longueur] > 0:
      print("{} : {}".format(longueur, histogramme[longueur]))
