n = int(input())
arr = []
for i in range(n):
    arr.append(sum(map(int,input().split())))
ans = 0
for x in arr:
    if x>1:
        ans+=1
print(ans)