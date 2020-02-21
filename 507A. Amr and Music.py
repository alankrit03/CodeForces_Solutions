n , k =map(int , input().split())

arr = [int(x) for x in input().split()]

arr = list(enumerate(arr))

arr.sort(key= lambda x:x[1])
total = 0
ans=[]
for x in arr:
    if total+x[1] > k:
        break
    else:
        total += x[1]
        ans.append(x[0]+1)

if ans:
    print(len(ans))
    print(*ans)
else:print(0)
# print(arr)