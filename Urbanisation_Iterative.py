n , n1, n2 = map(int,input().split())
arr=[int(x) for x in input().split()]

arr.sort(reverse=True)
temp=0
for i in range(min(n1,n2)):
    temp += arr[i]

ans= temp/min(n1,n2)
temp=0
x = i+1

for i in range(x , x+max(n1,n2)):
    temp += arr[i]
ans += temp/max(n1,n2)
print("{0:.8f}".format(ans))