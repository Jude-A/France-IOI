mois=int(input())
   
if mois==11 :
    print(29)
else :
    if mois>=4 and mois<=6 or mois==10 :
        print(31)
    else :
        print(30)
