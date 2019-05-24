baseSocle=int(input())
faceSocle=int(input())
volume=0

for loop in range(baseSocle-faceSocle+1) :
   volume+=baseSocle*baseSocle
   baseSocle-=1
print(volume)
