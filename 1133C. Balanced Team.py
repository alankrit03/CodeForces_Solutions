n = int(input())

arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

arr.sort()
ans = 1

i=j=0

while j<n:
    if j+1<n:

        if arr[j+1]-arr[i]<=5:
            j+=1
        else:
            ans = max(ans, (j-i+1))
            j+=1
            while i<=j and arr[j]-arr[i]>5:
                i+=1
    else:
        ans = max(ans, (j - i + 1))
        j+=1

print(ans)
