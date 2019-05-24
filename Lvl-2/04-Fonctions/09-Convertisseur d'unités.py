def extractUnité(valeur) :
   return valeur[len(valeur)-1]

def extractQuantité(valeur) :
   caracteres=list(valeur)
   caracteres[len(caracteres)-1]=" "
   valeur="".join(caracteres)
   return float(valeur)

nbConversions=int(input())

for loop in range(nbConversions) :
   valeur=input()
   unité=extractUnité(valeur)
   quantité=extractQuantité(valeur)
   if unité=="m" :
      quantité/=0.3048
      print(round(quantité,6),"p")
   elif unité=="g" :
      quantité*=0.002205
      print(round(quantité,6),"l")
   else :
      quantité=quantité*1.8+32
      print(round(quantité,6),"f")
