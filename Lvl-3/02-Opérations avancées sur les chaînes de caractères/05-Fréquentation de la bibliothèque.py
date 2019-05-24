somme=0

while True :
    try :
        somme+=sum(map(int,input().split(" ")))
    except :        
        print(somme)
        break
    
