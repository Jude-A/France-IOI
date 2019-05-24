from math import *

population=int(input())
croissance=float(input())

population*=(1+croissance/100)

print(floor(population))
