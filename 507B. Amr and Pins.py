r , x1 , y1 , x2 , y2 = map(int,input().split())
from math import sqrt,ceil
distance = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
# print(distance)
dia=int(2*r)
n=ceil(distance/dia)

print(n)