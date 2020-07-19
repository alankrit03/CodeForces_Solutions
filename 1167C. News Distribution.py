"""""""""""""""""""""""""""""""""""""""""""""""""""
Not Yet complete.
"""""""""""""""""""""""""""""""""""""""""""""""""""
n,m = map(int,input().split())
arr = [0]*m
used = [False]*m

for i in range(m):
    temp = input().split()
    k = int(temp[0])

    if k==0:
        used[i]=True

    temp2 = temp[1:]

    for j in range(k):
        temp2[j]=int(temp2[j])

    arr[i]=set(temp2)

print(arr)

ans = [1]*(n+1)

union_list = []

for i in range(m):
    if not used[i]:
        curr = arr[i]
        for j in range(i+1,m):
            if not curr.isdisjoint(arr[j]):
                curr.update(arr[j])
                used[j]=True
        union_list.append(list(curr))

print(union_list)

for union in union_list:
    k = len(union)
    for ele in union:
        ans[ele] = k

print(*ans[1:])