n , k =map(int,input().split())

arr = [int(x) for x in input().split()]

par = arr[k-1]

ans = 0
while ans<n and arr[ans]>0 and arr[ans]>=par:
    ans+=1

print(ans)