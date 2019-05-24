mot=input().upper()
phrase=input().upper()
phraseListe=phrase.split(" ")
compteMot=0

for i in range(len(phraseListe)):
    if mot==phraseListe[i]:
        compteMot+=1

print(compteMot)

    
