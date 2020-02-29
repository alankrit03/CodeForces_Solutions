n = int(input())

home = [0]*n
away = [0]*n

for i in range(n):
    home[i],away[i] = map(int,input().split())

from collections import defaultdict

diction = defaultdict(int)
for x in away:
    diction[x]+=1
ans = 0
for x in home:
    ans += diction.get(x,0)
print(ans)