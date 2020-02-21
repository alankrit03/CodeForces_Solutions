n = int(input())
arr = [int(x) for x in input().split()]
if n<3:
    print(0)
else:
    max_ele = arr[0]
    min_ele = arr[0]

    for i in range(n):
        if arr[i]>max_ele:
            max_ele=arr[i]
        elif arr[i]<min_ele:
            min_ele=arr[i]

    ans=0
    for i in range(n):
        if arr[i]>min_ele and arr[i]<max_ele:
            ans+=1

    print(ans)