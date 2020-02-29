k , dollars , banana = map(int , input().split())

total = k * (banana*(banana+1)//2)
temp = total-dollars
if temp>0:
    print(temp)

else:
    print(0)