n = int(input())
arr = [int(x) for x in input().split()]

min_val = 2000

for i in range(n-2):
    if min_val > arr[i+2]-arr[i]:
        min_val = arr[i+2]-arr[i]
        pos = i+1
ans = 0
for i in range(n-1):
    if i==pos:
        ans = max(ans, arr[i +1] - arr[i-1])
    else:
        ans = max(ans,arr[i+1]-arr[i])

print(ans)