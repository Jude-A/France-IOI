nbParticipants=int(input())
listeEntiers=[0]*nbParticipants

for entiers in range(nbParticipants) :
   listeEntiers[entiers]=int(input())
   
listeEntiers.sort()

maxListe=nbParticipants-1

for loop in range(nbParticipants//2) :
   print("{} {}".format(listeEntiers[loop],listeEntiers[maxListe]))
   maxListe-=1
