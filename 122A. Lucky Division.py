n = int(input())

lucky = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]

i=0

while i<14 and lucky[i]<=n:
    if n%lucky[i] == 0:
        print('YES')
        break
    i+=1
else:print('NO')