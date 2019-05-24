motDePasse=4242

def codeFaux() :
   mdpRentré=0
   while mdpRentré!=motDePasse :
      print("Entrez le code :")
      mdpRentré=int(input())

codeFaux()

print("Encore une fois.")

codeFaux()
   
print("Bravo.")
