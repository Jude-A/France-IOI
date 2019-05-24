taxeActuelle=float(input())
taxeFuture=float(input())
prixActuel=float(input())

prixFutur=(round(((prixActuel/(1+taxeActuelle/100))*(1+taxeFuture/100))*100))/100

print(prixFutur)
