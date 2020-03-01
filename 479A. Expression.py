a = int(input())
b = int(input())
c = int(input())

total =1

if a==1 and c==1:
    total = a+b+c
elif a==1 or (b==1 and a<=c):
    total = (a+b)*c
elif c==1 or (b==1 and c<=a):
    total = a* (b+c)
else:total = a*b*c

print(total)