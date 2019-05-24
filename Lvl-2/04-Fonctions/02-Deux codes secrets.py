def codeFaux(code) :
   mdpRentré=0
   while mdpRentré!=code :
      print("Entrez le code :")
      mdpRentré=int(input())

codeFaux(4242)

print("Premier code bon.")

codeFaux(2121)
   
print("Bravo.")
