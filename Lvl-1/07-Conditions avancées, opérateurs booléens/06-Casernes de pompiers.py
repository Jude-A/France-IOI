paireZones=int(input())

for loop in range(paireZones) :
   xMinA=int(input())
   xMaxA=int(input())
   yMinA=int(input())
   yMaxA=int(input())
   xMinB=int(input())
   xMaxB=int(input())
   yMinB=int(input())
   yMaxB=int(input())
   if xMinB>=xMaxA or xMaxB<=xMinA or yMinB>=yMaxA or yMaxB<=yMinA :
      print("NON")
   else :
      print("OUI")
