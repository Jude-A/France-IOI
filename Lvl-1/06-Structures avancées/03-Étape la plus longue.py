joursMarche=int(input())
record=0

for loop in range(joursMarche) :
   km=int(input())
   if km>record :
      record=km

print(record)
