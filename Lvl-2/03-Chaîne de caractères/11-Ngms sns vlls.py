for loop in range(2) :
   titre=input()
   for loop in range(len(titre)) :
      if titre[loop]!="A" and titre[loop]!="E" and titre[loop]!="I" and titre[loop]!="O" and titre[loop]!="U" and titre[loop]!="Y" and titre[loop]!=" " :
         print(titre[loop],end="")
   print()
