nbNotes=int(input())
noteTotal=0

for boucle in range(nbNotes) :
   note=int(input())
   noteTotal+=note
   
print(noteTotal/nbNotes)
