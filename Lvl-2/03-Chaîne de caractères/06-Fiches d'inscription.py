nbPersonnes=int(input())

for idPersonne in range(nbPersonnes) :
   prenomNom=input().split(" ")
   print("{} {}".format(prenomNom[1],prenomNom[0]))
