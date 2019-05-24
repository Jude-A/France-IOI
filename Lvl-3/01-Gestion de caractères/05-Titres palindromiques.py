nbLivres=int(input())

for livre in range(nbLivres):
    titre=input()
    titreMaj=titre.upper()
    titreSansEspaces=titreMaj.replace(" ","")
    if titreSansEspaces==titreSansEspaces[::-1]: #Slicing method, donnant une inversion de la chaine
        print(titre)
