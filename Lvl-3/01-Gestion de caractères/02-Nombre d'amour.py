enfant1,enfant2=input().split(" ")
tabEnfant1=[0]*len(enfant1)
tabEnfant2=[0]*len(enfant2)

for i in range(len(enfant1)) :
    tabEnfant1[i]=ord(enfant1[i])-65

for i in range(len(enfant2)) :
    tabEnfant2[i]=ord(enfant2[i])-65
    
nbEnfant1=sum(tabEnfant1)
nbEnfant2=sum(tabEnfant2)

while nbEnfant2>=10 or nbEnfant1>=10 :
    tabChiffresEnfant1=map(int,str(nbEnfant1))
    nbEnfant1=sum(tabChiffresEnfant1)
    tabChiffresEnfant2=map(int,str(nbEnfant2))
    nbEnfant2=sum(tabChiffresEnfant2)

print(nbEnfant1,nbEnfant2)
