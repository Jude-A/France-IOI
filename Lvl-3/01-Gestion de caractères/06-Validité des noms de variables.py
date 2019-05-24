def parcoursVarName(varname):
    for i in range(1,len(varname)):
        if not(varname[i].isalpha() or varname[i].isdigit() or varname[i]=="_"):
            return False
            break
    return True

nbNoms=int(input())

for nom in range(nbNoms):
    varName=input()
    if (varName[0].isalpha() or varName[0]=="_") and parcoursVarName(varName):
        print("YES")
    else:
        print("NO")
