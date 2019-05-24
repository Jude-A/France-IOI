nbMaisons=int(input())
xMax=0
xMin=1000000
yMax=0
yMin=1000000

for loop in range(nbMaisons) :
   x=int(input())
   y=int(input())
   if x>xMax :
      xMax=x
   if x<xMin :
      xMin=x
   if y>yMax :
      yMax=y
   if y<yMin :
      yMin=y

print(((yMax-yMin)+(xMax-xMin))*2)
